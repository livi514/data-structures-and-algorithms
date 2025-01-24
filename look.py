'''
LOOK algorithm. Like SCAN, but the direction can be changed at any point if no
more requests exist in the current direction
'''

top_floor_number = 10 #value can be any positive integer
number_of_floors = top_floor_number + 1 #top floor number + the ground_floor (floor 0)
direction_of_travel = "up" #can be "up" or "down"
current_floor = 10

#example requests - we will need to change the way that requests are processed for the real-time version of the algorithm
request_list = []

def lift():#Made this into a function so it calls everything within it
    global direction_of_travel, current_floor

    print(f"Elevator is ready! Current Floor: {current_floor}")
    print('Please type "exit" if you want to stop the program')

    #Step 1: Collecting the user floor input
    #Right now it just takes in one input. Will need to fix that
    while True:
        user_input = input(f"Enter a floor(0-{top_floor_number}) or type 'exit' to stop program: ").strip().lower() 
        if user_input == "exit": #This is an extra feature if you want the lift to stop before all the floors are done. Still woring on the listing part.
            print(f"Stopping Program. Remaining requests: {request_list}")
            break
        if (user_input.isnumeric()): #changed this to isnumeric() as the input can be any positive integer not just digits - Livi
            floor_request = int(user_input)

            #changed this to <= top_floor number rather than < top_floor number - Livi
            if 0 <= floor_request <= top_floor_number: #This checks if the floor request is within the ground floor(0) and top floor(10)
                request_list.append(floor_request)
                print(f"Added floor requests: {floor_request}")
            else: print(f"Invalid input. Please enter a valid floor number (0-{top_floor_number}) or type 'exit' to stop program: ")
        else:
          print(f'Please enter a valid floor number (0-{top_floor_number}) or type "exit" to stop program:')

        # This will process the requests in the current direction of the lift (step 2)
        while len(request_list) != 0:
            if direction_of_travel == "up":
                requests_sorted = sorted([request for request in request_list if request >= current_floor])
            else:  # direction_of_travel == "down"
                requests_sorted = sorted([request for request in request_list if request <= current_floor], reverse=True)
            if len(requests_sorted) == 0:
                if direction_of_travel == "down":
                    direction_of_travel = "up"  
                else:  # direction_of_travel == "up"
                    direction_of_travel = "down"
                print("Changing direction to", direction_of_travel)

            for floor in requests_sorted:
                current_floor = floor
                print("Current floor", floor)
                request_list.remove(floor)
                print("Remaining requests", request_list)

            if direction_of_travel == "up":
                if not any(requests > current_floor for requests in request_list):
                    direction_of_travel = "down"
            else:
                if not any(requests < current_floor for requests in request_list):
                    direction_of_travel = "up"
            print("Changing direction to", direction_of_travel)

lift()
