#not handling real-time requests at the moment
#Edited the lift function to compare lift direction and people getting off on a floor - Kim
def input_file():
    floor_requests = {}
    building_info = {}
    document = input("Please enter a lift file name: ")
    document = document.strip()
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
    except:
        print("File cannot be found, please try again.")


building_info, floor_requests = input_file()
top_floor = building_info["num_floors"]
bottom_floor = 1 #assuming 1 is the ground floor as there's no floor 0 in the input file examples?
current_floor = bottom_floor
direction_of_travel = "up"

#edited this function so that it handles capacity without affecting the building info - Livi 
def lift():
    global direction_of_travel, current_floor
    passengers = []
    max_capacity = building_info["capacity"]
    while True:
        #Dropping passengers
        passengers_to_drop = [p for p in passengers if p == current_floor]
        for p in passengers_to_drop:
            passengers.remove(p)
        if passengers_to_drop:
            print(f"Dropping off {len(passengers_to_drop)} passenger(s) at floor {current_floor}")
            print(f"Going {direction_of_travel}")
            print(f"Capacity available: {building_info['capacity']}")

        #Loading passengers into the lift
        if floor_requests.get(current_floor) and building_info["capacity"] > 0:
            while floor_requests[current_floor] and len(passengers) < max_capacity:
                passengers_getting_on = floor_requests[current_floor].pop(0)
                passengers.append(passengers_getting_on)
                print(f"Current passengers on lift: {passengers}")
                print(f"Going {direction_of_travel}")
                print(f"Floor {current_floor}")
                print(f"Remaining capacity: {building_info['capacity']}")

        #Checking if there are any more requests in the input file not fulfiled
        if not passengers and not any(floor_requests.values()):
            print("All requests fulfilled. Lift is idle.")
            print(f"Current Floor: {current_floor}")
            input("Please enter a floor") #why are we allowing the user to enter a floor here? - Livi
            print(f"Current state of the lift: {floor_requests}")
            break

        #Checking if the lift needs to change directions
        #I changed this code so that if there are no more requests in the current direction, the lift changes direction - Livi
        #setting requests_above and requests_below to False to begin with, these will be changed to True later if request are found below/above
        requests_above = False
        requests_below = False

        #checking all floor requests one by one
        for floor, requests in floor_requests.items():
            if requests:  #checking floors that have requests
                if floor > current_floor: #if a floor above the current floor has requests, then requests_above is set to True
                    requests_above = True
                    break #if we find a request above the current floor, we do not need to keep checking, so we can break out of the loop
                elif floor < current_floor: #if a floor below the current floor has requests, then requests_below is set to True
                    requests_below = True
                    break #if we find a request below the current floor, we do not need to keep checking, so we can break out of the loop

        #deciding if the lift should change direction
        #if we have no more requests in the current direction or we reach the top/bottom floor, the lift switches directions
        if direction_of_travel == "up":
            if current_floor == top_floor or not requests_above:
                direction_of_travel = "down" 
        elif direction_of_travel == "down":
            if current_floor == bottom_floor or not requests_below:
                direction_of_travel = "up"

        #moving the lift to the next floor
        if direction_of_travel == "up":
            current_floor += 1
        else:
            current_floor -= 1

lift()