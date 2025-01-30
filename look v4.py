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
                num_floors, capcity = map(int, line.split(","))
                building_info["num_floors"] = num_floors
                building_info["capacity"] = capcity
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
    if direction_of_travel == "up":
        for floor in range(current_floor, top_floor+1):
            print(f"Lift is at floor {floor}")
            #will add code later
    else:
        for floor in range(current_floor, bottom_floor):
            print(f"Lift is at floor {floor}")
            #will add code later

lift()
