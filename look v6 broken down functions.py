#Edited the lift function to compare lift direction and people getting off on a floor - Kim
def input_file():
     while True:
        floor_requests = {}
        building_info = {}
        document = input("Please enter a lift file name: ").strip()
        # Handle file extension
        if not document.endswith(".txt"):
            document += ".txt"
        #added exception handling - Livi
        try:
            with open(document) as f:
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
            print(f"Error: The file '{document}' cannot be found. Please try again.")
        except ValueError:
            print(f"Error: Invalid file format, please try again.")
        except Exception as e:
            print(f"An unexpected error occured: {e}. Please try again.")

building_info, floor_requests = input_file()
top_floor = building_info["num_floors"]
bottom_floor = 1
current_floor = bottom_floor
direction_of_travel = "up"

#broke down the lift function into smaller functions - Livi
def dropping_passengers(passengers_on_board, current_floor):
    passengers_to_drop = [p for p in passengers_on_board if p == current_floor]
    passengers_on_board = [p for p in passengers_on_board if p != current_floor]

    if passengers_to_drop:
        print(f"Dropping off {len(passengers_to_drop)} passenger(s) at floor {current_floor}")
        print(f"Going {direction_of_travel}")
        print(f"Capacity available: {len(passengers_on_board)}")
    return passengers_to_drop, passengers_on_board

def picking_up_passengers(passengers_on_board, current_floor, max_capacity):
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
            print(f"Remaining capacity: {max_capacity - len(passengers_on_board)}")
    return new_passengers, passengers_on_board
    
def new_requests(passengers_on_board, current_floor):
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

def changing_direction(current_floor, direction_of_travel, passengers_on_board):
    #Checking if the lift needs to change directions
    #I changed this code so that if there are no more requests in the current direction, the lift changes direction - Livi
    requests_above = any(floor > current_floor and floor_requests[floor] for floor in floor_requests)
    requests_below = any(floor < current_floor and floor_requests[floor] for floor in floor_requests)

    #deciding if the lift should change direction
    #if we have no more requests in the current direction or we reach the top/bottom floor, the lift switches directions
    if direction_of_travel == "up" and not requests_above:
        direction_of_travel = "down" 
    elif direction_of_travel == "down" and not requests_below:
        direction_of_travel = "up"
    return direction_of_travel

def moving_lift(current_floor):
    if direction_of_travel == "up":
        if current_floor < top_floor:
            current_floor += 1
    else:
        current_floor -= 1
    return current_floor
    
#edited this function so that it handles capacity without affecting the building info - Livi 
def lift():
    global direction_of_travel, current_floor, floor_requests
    passengers_on_board = []
    max_capacity = building_info["capacity"]

    while True:
        passengers_to_drop, passengers_on_board = dropping_passengers(current_floor, passengers_on_board)

        new_passengers, passengers_on_board = picking_up_passengers(current_floor, passengers_on_board, max_capacity)

        floor_requests, exit = new_requests(current_floor, passengers_on_board)
        if exit:
            break

        exit = checking_for_requests(current_floor, passengers_on_board)
        if exit:
            break

        direction_of_travel = changing_direction(current_floor, direction_of_travel)
        
        if any(floor_requests.values()) or passengers_on_board:  # Prevent unnecessary movement
            current_floor = moving_lift(current_floor, direction_of_travel) 

lift()