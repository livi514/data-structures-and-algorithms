'''
SCAN algorithm. This algorithm has the lift move in one direction and only
changes direction when it reaches the bottom or top floors. It serves all requests
while travelling in that direction
'''
import time

def input_file():
    while True:
        floor_requests = {}
        building_info = {}
        document = input("Please enter a lift file name: ").strip()
        #editing the code so that it can handle the input whether the user includes ".txt" at the end or not - Livi
        if document.endswith(".txt"):
            file = document
        else:
            file = document + ".txt"
        #added exception handling - Livi
        try:
            with open(file) as f:
                for line in f:
                    line = line.strip()
                    #print(line)
                    if line.startswith("#") or not line:
                        continue # This will skip the comments and any empty line -Kim

                    if "," in line and ":" not in line:
                        num_floors, capacity = map(int, line.split(","))
                        building_info["num_floors"] = num_floors
                        building_info["capacity"] = capacity
                        continue

                    floor, requests = line.split(":")
                    floor = int(floor.strip())
                    requests = [int(r) for r in requests.split(",") if r.strip()] #Converting the values into integers
                    floor_requests[floor] = requests #Putting the values into the dictionary
                print("Building information:")
                print(f"Number of floors: {building_info['num_floors']}")
                print(f"Lift capacity: {building_info['capacity']} \n")

                print("Floor Requests:")
                for floor, requests in floor_requests.items():
                    print(f"  Floor {floor}: {requests if requests else 'No requests'}")
                return building_info, floor_requests
        except FileNotFoundError:
            print(f"Error: The file '{file}' cannot be found. Please try again.")
        except ValueError:
            print(f"Error: Invalid file format, please try again.")
        except Exception as e:
            print(f"An unexpected error occured: {e}. Please try again.")

building_info, floor_requests = input_file()
top_floor = building_info["num_floors"]
bottom_floor = 1 #assuming 1 is the ground floor as there's no floor 0 in the input file examples?
current_floor = bottom_floor
direction_of_travel = "up"

def dropping_passengers(passengers_on_board):
  passengers_to_drop = [p for p in passengers_on_board if p == current_floor]
  passengers_on_board = [p for p in passengers_on_board if p != current_floor]

  if passengers_to_drop:
    print(f"Dropping off {len(passengers_to_drop)} passenger(s) at floor {current_floor}")
    print(f"Going {direction_of_travel}")
    print(f"Capacity available: {len(passengers_on_board)}")
    return passengers_to_drop, passengers_on_board
  
def picking_up_passengers(passengers_on_board, max_capacity):
    new_passengers = []
    if floor_requests.get(current_floor):
        while floor_requests[current_floor] and len(passengers_on_board) < max_capacity:
            new_passenger = floor_requests[current_floor].pop(0)
            passengers_on_board.append(new_passenger)
            new_passengers.append(new_passenger)
        if new_passengers:
            print(f"Picking up {len(new_passengers)} passenger(s) at floor {current_floor}")
            print(f"Current passengers on lift: {passengers_on_board}")
            print(f"Going {direction_of_travel}")
            print(f"Floor {current_floor}")
            print(f"Remaining capacity: {max_capacity -len(passengers_on_board)}")
    return new_passengers, passengers_on_board

def new_requests(passengers_on_board):
    user_input = input("Please enter a floor for a new request or press enter if there are no new requests. Enter 'exit' to stop the program: ") #gave them an option if there are no new requests but they still want to continue the program - Livi
    print(f"New user input: {user_input}")
    exit = False
    if user_input == "exit":
        print("Lift is stopping.")
        exit = True
    elif user_input.strip() == "": #if there are no new requests but the program is continuing - Livi
        print("No new requests.")
        print(f"Current passengers on lift: {passengers_on_board}")
    elif user_input.isdigit():
        new_floor = int(user_input)
        if new_floor == current_floor: #added this so that the request can't be the same as the current floor - Livi
            print(f"Passenger is already at floor {new_floor}.") #this message is printed, and the request is ignored/not added to the list - Livi
        elif 1 <= new_floor <= top_floor:#Checking if the input is within the building for info
            print(f"New request added: floor {current_floor} -> {new_floor}")
            floor_requests.setdefault(current_floor, []).append(new_floor) #tried editing this but it's not helping - Livi
            print(f"Current passengers on lift: {passengers_on_board}")
        else:
            print(f"Invalid input. Please enter a floor between 1 and {top_floor}.")
    else:
        print(f"Invalid input. Please enter a floor between 1 and {top_floor}, press  enter if there are no new requests, or enter 'exit' to stop the program.")
    return floor_requests, exit

def checking_for_requests(passengers_on_board):
    exit = False
    if not passengers_on_board and not any(floor_requests.values()):
        print("All requests fulfilled. Lift is idle.")
        print(f"Current Floor: {current_floor}")
        print(f"Current state of the lift: {floor_requests}")
        exit = True
    return exit

def changing_direction(current_floor, direction_of_travel):
    if direction_of_travel == "up" and current_floor == top_floor:
        direction_of_travel = "down" 
    elif direction_of_travel == "down" and current_floor == bottom_floor:
        direction_of_travel = "up"
    return direction_of_travel

def moving_lift(current_floor):
    if direction_of_travel == "up":
        if current_floor < top_floor:
            current_floor += 1
    else:
        current_floor -= 1
    return current_floor

def lift():
    global direction_of_travel, current_floor
    passengers_on_board = []
    max_capacity = building_info["capacity"]

    while True:

        passengers_to_drop, passengers_on_board = dropping_passengers(passengers_on_board)
        
        # Picking up passengers (while within capacity)
        new_passengers, passengers_on_board = picking_up_passengers(passengers_on_board, max_capacity)

        floor_requests, exit = new_requests(passengers_on_board)
        if exit == True:
            break #exits the lift() function and stops the execution of the lift

        #Checking if there are any more requests in the input file not fulfiled
        exit = checking_for_requests(passengers_on_board)
        if exit == True:
            break

        #checking if we need to change direction, changing direction if needed
        direction_of_travel = changing_direction(current_floor, direction_of_travel)
        
        #moving the lift to the next floor
        current_floor = moving_lift(current_floor)  

lift()



#previous code:   

'''
print(f"Starting at floor {currentFloor}")
while upRequests or downRequests:
  # sort requests depending on the direction fo travel
  if direction == "up":
    requests=upRequests
    requests.sort()
    floorInc = 1
  else:
    requests=downRequests
    requests.sort(reverse=True)
    floorInc = -1

  print(requests)
  print(f"Lift going {direction}")

  for floor in requests[:]:
    if (direction == "up" and floor >= currentFloor) or \ 
       (direction == "down" and floor <= currentFloor):
         while (currentFloor != floor):
           currentFloor += floorInc
           time.sleep(0.25)
           print(f"Stopping at floor {floor}")
           time.sleep(1)
           currentFloor = floor
           if direction == "up":
             upRequests.remove(floor)
           else:
             downRequests.remove(floor)
'''
