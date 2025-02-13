#will continue comments and docstrings later - Livi
def input_file():
    '''
    Processes an input file, storing the number of floors and capacity of the lift in the dictionary "building_info" and the requests at each floor in "floor_requests.

    Args: None

    Returns:

    '''
    while True:
        #initialising floor_requests and building_info as empty dictionaries
        floor_requests = {} #key - floor number, value - a list of floor numbers representing the floors that the passengers on that floor want to go to
        building_info = {} #stores the number of floors and the lift's capacity
        document = input("Please enter a lift file name: ").strip().lower() #allowing the user to input the name of the file to load, the file will contain the current floor requests 
   
        #handling the user input whether they include ".txt" at the end or not
        if document.endswith(".txt"):
            file = document
        else:
            file = document + ".txt" #concatenating ".txt" to the end of the user input, if the user has not already included it
        
        #reading the file line-by-line, and storing any important information
        try: #using exception handling in case the fie is not found, the user inputs an invalid file name, or another error occurs
            with open(file) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#") or not line:
                        continue #skipping comments and empty lines as these don't contain any important information to store, continue starts the next iteration

                    if "," in line and ":" not in line: #this means that the line contains the number of floors in the building and the capacity of the lift
                        num_floors, capacity = map(int, line.split(",")) #splitting at the comma, the first digit is the number of floors, the second is the capacity
                        #storing the number of floors and capacity in building_info
                        building_info["num_floors"] = num_floors 
                        building_info["capacity"] = capacity
                        continue #starting the next iteration as we have already dealt with this line

                    #if we haven't handled the line yet, then this will be a line containing a floor and all the requests from that floor
                    floor, requests = line.split(":") #splitting at the colon: before the colon - the floor, after the colon - all the requests from that floor
                    floor = int(floor.strip()) #assiging the digit before the colon to floor, removing any whitespace and converting it to an integer 
                    requests = [int(r) for r in requests.split(",") if r.strip()] #splitting the values after the colon at the commas, stripping each value of whitespace, converting it to an int and adding it to the requests list
                    floor_requests[floor] = requests #Putting the values into the dictionary

                #displaying the building information - the number of floors and capacity of the lift
                print("Building information:")
                print(f"Number of floors: {building_info['num_floors']}")
                print(f"Lift capacity: {building_info['capacity']} \n")

                #displaying the requests from each floor
                print("Floor Requests:")
                for floor, requests in floor_requests.items():
                    print(f"  Floor {floor}: {requests if requests else 'No requests'}") #printing ghe floor number, and "No requests" if the requests list for that floor is empty, otherwise, printing the request list
                return building_info, floor_requests #returning these so they can be used by the lift() function, and the functions called from lift()
            
        except FileNotFoundError: #if the file cannot be found
            print(f"Error: The file '{file}' cannot be found. Please try again.")
        except ValueError: #if the format of the file is invalid
            print(f"Error: Invalid file format, please try again.")
        except Exception as e: #any other exceptions
            print(f"An unexpected error occured: {e}. Please try again.")

def dropping_passengers(current_floor, passengers_on_board, direction_of_travel, floor_requests):
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

def picking_up_passengers(current_floor, passengers_on_board, floor_requests, max_capacity, direction_of_travel):
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
    return not passengers_on_board and all(not reqs for reqs in floor_requests.values())

'''
def checking_for_requests(passengers_on_board, floor_requests):
    """Checking if there are any remaining requests"""
    """if not passengers_on_board and not any(floor_requests.values()):
        print("All requests fulfilled. Lift is idle.")
        print(f"Current Floor: {current_floor}")
        print(f"Current state of the lift: {floor_requests}")
        return True
    return False"""
    return not passengers_on_board and not any(floor_requests.values())#commented the above out and made it to return True if it there are no passengers or pending requests - Kim
'''

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
    """Main lift simulation"""
    building_info, floor_requests = input_file()
    top_floor = building_info["num_floors"]
    bottom_floor = 1
    current_floor = bottom_floor
    direction_of_travel = "up"
    passengers_on_board = []

    while True:
        passengers_on_board = dropping_passengers(current_floor, passengers_on_board, direction_of_travel, floor_requests)
        passengers_on_board = picking_up_passengers(current_floor, passengers_on_board, floor_requests, building_info['capacity'], direction_of_travel)

        floor_requests, exit_program = new_requests(current_floor, floor_requests, top_floor)
        if exit_program:
            break

        # Clean up empty requests
        floor_requests = {floor: reqs for floor, reqs in floor_requests.items() if reqs}

        if checking_for_requests(passengers_on_board, floor_requests):
            break

        direction_of_travel = changing_direction(current_floor, direction_of_travel, floor_requests)
        if any(floor_requests.values()) or passengers_on_board:
            current_floor = moving_lift(current_floor, direction_of_travel)

lift()
