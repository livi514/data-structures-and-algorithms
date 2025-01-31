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
    if direction_of_travel == "up":
        for floor in range(current_floor, top_floor+1):
            print(f"Lift is at floor {floor}")
            
            '''
            To dos (use similar logic for travelling downwards)
            We should have people get off the lift first, and then new people get on.
            - adjust capacity based on length of value associated with that floor
            '''
            #this is to check who's getting off at this floor
            for i in range(1, floor+1):
                if i in floor_requests[floor]:
                    floor_requests[floor].remove(i)
                    building_info["capacity"] += 1 #since one person got off

            requests_at_floor = floor_requests[floor]
            num_people_at_floor = len(requests_at_floor)
            while building_info["capacity"] > 0:
                building_info["capacity"] -= num_people_at_floor
                if building_info["capacity"] == 0:
                    print("No more space left on the lift.")
                    #some logic idk - need to continue to the next floor because maybe people will get off there
            
    else:
        for floor in range(current_floor, bottom_floor):
            print(f"Lift is at floor {floor}")

lift()
