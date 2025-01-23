'''
LOOK algorithm. Like SCAN, but the direction can be changed at any point if no
more requests exist in the current direction
'''

#number of floors - any positive integer
number_of_floors = 10

#direction of travel - "up" or "down"
direction_of_travel = "up"

current_floor = 0

TOP_FLOOR = number_of_floors
BOTTOM_FLOOR = 0

#will be updated to true later on
top_floor_reached = False

#lift will start on the ground floor?
bottom_floor_reached = True

#for now, I'm not implementing priorities 

#just making up some requests so far - for real time I think we have to let users input them somehow?
request_list = [8, 7, 2, 5, 6]  

#here, a lift journey will be either the lift travelling downwards or upwards, when the lift changes direction, this will begin a new "journey"
def lift_journey():
  global current_floor, direction_of_travel, request_list
  #for now I haven't implemented different priorities
  #sorting the list in ascending or descending order based on the direction of travel 
  #e.g. if we're going up we'll start with the request with the lowest number
  if direction_of_travel == "up":
    #sorting the list in ascending order
    request_list.sort()
  elif direction_of_travel == "down":
    request_list.sort(reverse=True)
  floors = list(range(number_of_floors + 1))
  for i in range(number_of_floors+1):
    floors.append(i)
  for i in floors:
    current_floor = i
    print("Current floor:" , current_floor)
    if i in request_list:
      request_list.remove(i)
      print("Request list:", request_list)
    if (current_floor == TOP_FLOOR) or (len(request_list == 0)): #this means we can turn the lift around
      if direction_of_travel == "up":
        direction_of_travel == "down"
      elif direction_of_travel == "down":
        direction_of_travel == "up"
      print(direction_of_travel)
      break

lift_journey()

