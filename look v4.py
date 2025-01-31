#not handling real-time requests at the moment

def input_file():
    floor_requests = {}
    building_info = {}
    with open("input.txt") as f:
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

building_info, floor_requests = input_file()
top_floor = building_info["num_floors"]
bottom_floor = 1 #assuming 1 is the ground floor as there's no floor 0 in the input file examples?
current_floor = bottom_floor
direction_of_travel = "up"

def lift():
    global direction_of_travel, current_floor
    passengers = []
    while True:
        passengers_to_remove = [p for p in passengers if p == current_floor]
        while ((floor_requests[current_floor]) and building_info["capacity"] > 0):
            passenger_getting_on = floor_requests[current_floor].pop(0)
            passengers.append(passenger_getting_on)
            building_info["capacity"] -= 1

        if direction_of_travel == "up":
            current_floor += 1
        else:
            current_floor -= 1

        if not passengers and not any(floor_requests.values()):
            print("All requests fulfilled. Lift is idle.")
            break

lift()
