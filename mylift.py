import os

"""This code is an improvement to look.py adding in features such as priority"""

def input_file():
    """Reads the lift configuration file and extracts buildinf ifo and floor if the file is present"""
    while True:
        file_name = input("Enter lift file name: ").strip()
        file_name += ".txt" if not file_name.endswith(".txt") else ""

        if not os.path.exists(file_name):
            print(f"Error: '{file_name}' not found. Please chack your availiable file and try again.")
            continue
        building_info, floor_requests = {}, {}
        try:
            with open(file_name) as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"): #it will ignore comments in the file
                        continue
                    if "," in line and ":" not in line:
                        building_info["num_floors"], building_info["capacity"] = map(int, line.split(","))
                    else:
                        floor, requests = line.split(":")
                        floor_requests[int(floor)] = [int(r) for r in requests.split(",") if r.strip()]

            return building_info, floor_requests
        except ValueError:
            print("Error: Invalid file format. Try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Function to drop passengers at the current floor the lift moved to
def drop_passengers(current_floor, passengers, building_info):
    """Handles passengers drop-offs at the current floor"""
    departing = [p for p in passengers if p == current_floor]#Gets the lists of passengers gettign off at the current floor
    passengers = [p for p in passengers if p != current_floor]#Removes them from the list
    if departing:
        print(f"Dropping off {len(departing)} passenger(s) at floor {current_floor}")
    return passengers

# Function to pick up passengers from the floor
def pick_up_passengers(current_floor, passengers, floor_requests, max_capacity, direction):
    """Handles picking up passengers from the current floor based on priority in the current direction."""
    if current_floor in floor_requests:
        floor_requests[current_floor].sort(key=lambda x: (direction == "up" and x < current_floor, direction == "down" and x > current_floor))
        while floor_requests[current_floor] and len(passengers) < max_capacity:
            passengers.append(floor_requests[current_floor].pop(0))
    return passengers

# Function to handle new real-time requests
def new_requests(current_floor, floor_requests, top_floor, passengers):
    """This allows for real-time from user input"""
    user_input = input("Enter a floor (or 'exit' to stop the lift): ").strip()
    if user_input.lower() == "exit":
        return floor_requests, True
    elif user_input.isdigit():
        new_floor = int(user_input)
        if 1 <= new_floor <= top_floor and new_floor != current_floor:
            floor_requests.setdefault(current_floor, []).append(new_floor)
    return floor_requests, False

# Function to change the direction of lift
def change_direction(current_floor, direction, floor_requests, passengers):
    """This function is to determine if the lift should change direction based on remaining requests and the priorities."""
    requests_above = any(floor > current_floor for floor in floor_requests if floor_requests[floor]) or any(p > current_floor for p in passengers)
    requests_below = any(floor < current_floor for floor in floor_requests if floor_requests[floor]) or any(p < current_floor for p in passengers)
    if direction == "up" and not requests_above and requests_below:
        return "down"
    if direction == "down" and not requests_below and requests_above:
        return "up"
    return direction

# Function to move the lift up or down
def move_lift(current_floor, direction):
    """Moves the lift one floor in the current direction."""
    return current_floor + 1 if direction == "up" else current_floor - 1

# Main function controlling the lift operations
def lift_system():
    """This is the main function of the lift operations"""
    building_info, floor_requests = input_file()
    top_floor, capacity = building_info["num_floors"], building_info["capacity"]
    current_floor, direction, passengers = 1, "up", []

    while True:
        print(f"Lift at floor {current_floor}, going {direction}")
        print(f"Current passengers: {passengers}")
        print(f"Requests on each floor: {floor_requests}")
        
        passengers = drop_passengers(current_floor, passengers, building_info)
        passengers = pick_up_passengers(current_floor, passengers, floor_requests, capacity, direction)
        floor_requests, stop = new_requests(current_floor, floor_requests, top_floor, passengers)
        if stop:
            break
        if not passengers and not any(floor_requests.values()):
            print("All requests fulfilled. Lift is idle.")
            break
        direction = change_direction(current_floor, direction, floor_requests, passengers)
        current_floor = move_lift(current_floor, direction)

# Run the lift system if the script is executed
if __name__ == "__main__":
    lift_system()

