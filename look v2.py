'''
For this version, I'm trying to implement real-time processing.
I'm going to add a time delay associated with moving between floors.
At each floor, the program will check for new requests (the user will be able to input these).
- Livi
'''

'''
LOOK algorithm. Like SCAN, but the direction can be changed at any point if no
more requests exist in the current direction
'''

import time

top_floor_number = 10 #value can be any positive integer
number_of_floors = top_floor_number + 1 #top floor number + the ground_floor (floor 0)
direction_of_travel = "up" #can be "up" or "down"
current_floor = 10
time_between_floors = 2 #time it takes to travel between one floor to the next, in seconds

people_getting_on = []
people_getting_off = []
    
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
                if floor_request not in request_list: #checking whether the request is already in the list to avoid duplicates 
                    request_list.append(floor_request)
                else:
                    print(f"Floor {floor_request} is already in the request list.")

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
                continue #added continue to stop the loop from iterating again once the requests have all been dealt with - Livi

            for floor in requests_sorted:
                current_floor = floor
                print("Current floor", floor)

                #new bit I added with the time delay and real-time requests -------------------------------------------
                start_time = time.time()
                while time.time() - start_time < time_between_floors:
                    user_input = input(f"Enter a floor(0-{top_floor_number}) or press 'enter' if there are no new requests currently. Type 'exit' to stop the program: ").strip().lower()
                    if user_input.isnumeric():
                        new_floor_request = int(user_input)
                        if 0 <= new_floor_request <= top_floor_number:
                            if new_floor_request not in request_list:
                                request_list.append(new_floor_request)
                                print(f"Added floor request: {new_floor_request}")
                            else:
                                print(f"Floor {new_floor_request} is already in the request list.")
                        else:
                            print(f"Invalid floor. Enter between 0 and {top_floor_number}.")
                    elif new_floor_request == "exit":
                        print(f"Stopping Program. Remaining requests: {request_list}")
                        break

                request_list.remove(floor)
                print("Remaining requests", request_list)

            if (direction_of_travel == "up") and (not any(requests > current_floor for requests in request_list)):
                    direction_of_travel = "down"
            elif (direction_of_travel == "down") and (not any(requests < current_floor for requests in request_list)):
                    direction_of_travel = "up"
            print("Changing direction to", direction_of_travel)

lift()
