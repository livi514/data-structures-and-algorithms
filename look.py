'''
LOOK algorithm. Like SCAN, but the direction can be changed at any point if no
more requests exist in the current direction
'''

#number of floors - any positive integer
number_of_floors = 10

#direction of travel - "up" or "down"
direction_of_travel = "up"

TOP_FLOOR = number_of_floors
BOTTOM_FLOOR = 0

#will be updated to true later on
top_floor_reached = False

#lift will start on the ground floor?
bottom_floor_reached = True

#for now, I'm not implementing priorities 

#just making up some requests so far - for real time I think we have to let users input them somehow?
request_list = [10, 7, 2, 5, 6]  

#here, a lift journey will be either the lift travelling downwards or upwards, when the lift changes direction, this will begin a new "journey"
def lift_journey():
  #for now I haven't implemented different priorities
  #sorting the list in ascending or descending order based on the direction of travel 
  #e.g. if we're going up we'll start with the request with the lowest number
  if direction_of_travel == "up":
    #sorting the list in ascending order
    request_list.sort()
  elif direction_of_travel == "down":
    request_list.sort(reverse=True)
  floors = []
  for i in range(number_of_floors):
    floors.append(i)
  print(floors)

lift_journey()

