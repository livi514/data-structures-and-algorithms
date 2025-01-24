'''
LOOK algorithm. Like SCAN, but the direction can be changed at any point if no
more requests exist in the current direction
'''

#CURRENTLY DEBUGGING

#ground floor - floor number 0

top_floor_number = 10 #value can be any positive integer
number_of_floors = top_floor_number + 1 #top floor number + the ground floor (floor 0)
direction_of_travel = "up" #can be "up" or "down"
current_floor = 10

#example requests - we will need to change the way that requests are processed for the real-time version of the algorithm 
request_list = [6, 2, 8, 7, 5]

'''
while len(request_list) != 0:
  if direction_of_travel == "up":
    requests_sorted = sorted([request for request in request_list if request >= current_floor])
  else: #direction_of_travel == "down"
    requests_sorted = sorted([request for request in request_list if request <= current_floor], reverse=True)
  if len(requests_sorted) == 0:
    if direction_of_travel == "down":
      direction_of_travel == "up"
    else: #direction_of_travel == "up"
      direction_of_travel == "down"
    print("Changing direction to", direction_of_travel)
  
  for floor in requests_sorted:
    current_floor = floor
    print("Current floor", floor)
    request_list.remove(floor)
    print("Remaining requests", request_list)

  
  if direction_of_travel == "up":
    if not any (requests > current_floor for requests in request_list):
      direction_of_travel == "down"
  else:
    if not any (requests < current_floor for requests in request_list):
      direction_of_travel == "up"
  print("Changing direction to", direction_of_travel)
'''

