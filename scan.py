'''
SCAN algorithm. This algorithm has the lift move in one direction and only
changes direction when it reaches the bottom or top floors. It serves all requests
while travelling in that direction
'''
import time

print(f"Starting at floor {currentFloor}")
while upRequests or downRequests:
  # sort requests depending on the direction fo travel
  if direction == "up":
    requests=upRequests
    requests.sort()
    floorInc = 1
  else:
    requests=downRequests
    requests.sort(reverse=True)
    floorInc = -1

  print(requests)
  print(f"Lift going {direction}")

  for floor in requests[:]:
    if (direction == "up" and floor >= currentFloor) or \ 
       (direction == "down" and floor <= currentFloor):
         while (currentFloor != floor):
           currentFloor += floorInc
           time.sleep(0.25)
           print(f"Stopping at floor {floor}")
           time.sleep(1)
           currentFloor = floor
           if direction == "up":
             upRequests.remove(floor)
           else:
             downRequests.remove(floor)

  
