#not handling real-time requests at the moment
#Edited the lift function to compare lift direction and people getting off on a floor - Kim
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


#broke down the lift function into smaller functions - Livi
def dropping_passengers(current_floor, passengers_on_board, direction_of_travel):
        """This function is called to drop off passengers on designated floors"""
        passengers_to_drop = [p for p in passengers_on_board if p == current_floor]
        passengers_on_board = [p for p in passengers_on_board if p != current_floor]
        if passengers_to_drop:
            print(f"Dropping off {len(passengers_to_drop)} passenger(s) at floor {current_floor}")
            print(f"Going {direction_of_travel}")
            print(f"Floor {current_floor}")
            print(f"Capacity available: {len(passengers_on_board)}")
            print(f"Current passengers on lift: {len(passengers_on_board)}")
            print(f"Current floor requests: {floor_requests}")

        return passengers_on_board

def picking_up_passengers(current_floor, passengers_on_board,  floor_requests, max_capacity):
    """This will pick up new passengers in there is space on the lift"""
    new_passengers = []
    if current_floor in floor_requests:
        while floor_requests[current_floor] and len(passengers_on_board) < max_capacity:
            new_passenger = floor_requests[current_floor].pop(0)
            passengers_on_board.append(new_passenger)
            new_passengers.append(new_passenger)

        if new_passengers:
            print(f"Picking up {len(new_passengers)} passenger(s) at floor {current_floor}")
            print(f"Current passengers on lift: {len(passengers_on_board)}")
            print(f"Current floor requests: {floor_requests}")
            print(f"Going {direction_of_travel}")
            print(f"Floor {current_floor}")
            print(f"Remaining capacity: {max_capacity -len(passengers_on_board)}")
    
    return passengers_on_board
    
def new_requests(current_floor, floor_requests, top_floor):
    """Allows for real time requests"""
    user_input = input("Please enter a floor for a new request or press enter if there are no new requests. Enter 'exit' to stop the program: ") #gave them an option if there are no new requests but they still want to continue the program - Livi
    print(f"New user input: {user_input}")
    
    if user_input == "exit":
        print("Lift is stopping.")
        print(f"Current requests: {floor_requests}")
        return floor_requests, True
    

    elif user_input.strip() == "": #if there are no new requests but the program is continuing - Livi
        print("No new requests.")
        print(f"Current passengers on lift: {floor_requests}")
    
    if user_input.isdigit():
        new_floor = int(user_input)
        if new_floor == current_floor: #added this so that the request can't be the same as the current floor - Livi
            print(f"Passenger is already at floor {new_floor}.") #this message is printed, and the request is ignored/not added to the list - Livi
        elif 1 <= new_floor <= top_floor:#Checking if the input is within the building for info
            print(f"New request added: floor {current_floor} -> {new_floor}")
            if current_floor not in floor_requests:
                floor_requests[current_floor] = [] # Issue with updating the dictionary.Not sure how to fix that yet - Kim
            floor_requests[current_floor].append(new_floor)
            print(f"Current passengers on lift: {floor_requests}")
        else:
            print(f"Invalid input. Please enter a floor between 1 and {top_floor}.")
    
    return floor_requests, False

def checking_for_requests(passengers_on_board, floor_requests):
    """Checking if there are any remaining requests"""
    """if not passengers_on_board and not any(floor_requests.values()):
        print("All requests fulfilled. Lift is idle.")
        print(f"Current Floor: {current_floor}")
        print(f"Current state of the lift: {floor_requests}")
        return True
    return False"""
    return not passengers_on_board and not any(floor_requests.values())#commented the above out and made it to return True if it there are no passengers or pending requests - Kim

def changing_direction(current_floor, direction_of_travel, floor_requests):
    #Checking if the lift needs to change directions
    #I changed this code so that if there are no more requests in the current direction, the lift changes direction - Livi
    requests_above = any(floor > current_floor and floor_requests.get(floor) for floor in floor_requests)
    requests_below = any(floor < current_floor and floor_requests.get(floor) for floor in floor_requests)

    #deciding if the lift should change direction
    #if we have no more requests in the current direction or we reach the top/bottom floor, the lift switches directions
    if direction_of_travel == "up" and not requests_above:
        direction_of_travel = "down" 
    elif direction_of_travel == "down" and not requests_below:
        direction_of_travel = "up"

    return direction_of_travel

def moving_lift(current_floor, direction_of_travel):
    """Should move the lift up and down"""
    return current_floor + 1 if direction_of_travel == "up" else current_floor - 1
    
#edited this function so that it handles capacity without affecting the building info - Livi 
def lift():
    """Main lift simulation""" #- Kim
    global direction_of_travel, current_floor, top_floor, floor_requests
    building_info, floor_requests = input_file()
    top_floor = building_info["num_floors"]
    bottom_floor = 1 #assuming 1 is the ground floor as there's no floor 0 in the input file examples?
    current_floor = bottom_floor
    direction_of_travel = "up"
    passengers_on_board = [] #having issues with this

    while True:
        passengers_on_board = dropping_passengers(current_floor, passengers_on_board, direction_of_travel)
        passengers_on_board = picking_up_passengers(current_floor, passengers_on_board, floor_requests, building_info['capacity'])
        
        floor_requests, exit_program = new_requests(current_floor, floor_requests, top_floor)
        if exit_program:
            break
        
        if checking_for_requests(passengers_on_board, floor_requests):
            break
        
        direction_of_travel = changing_direction(current_floor, direction_of_travel, floor_requests)
        if any(floor_requests.values()) or passengers_on_board:
            current_floor = moving_lift(current_floor, direction_of_travel)

lift()
