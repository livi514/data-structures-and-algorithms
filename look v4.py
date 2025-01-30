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
input_file()

top_floor = #idk how i'd get this
direction_of_travel = "up"

def lift():
    global direction_of_travel, current_floor
    if direction_of_travel == "up":
        for i in range(current_floor, top_floor):
            break
            #will add code later
    else:
        for i in range(current_floor, bottom_floor):
            break
            #will add code later
