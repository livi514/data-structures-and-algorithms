'''
SCAN algorithm. This algorithm has the lift move in one direction and only
changes direction when it reaches the bottom or top floors. It serves all requests
while travelling in that direction
'''
def ElevatorScan(requests, CurrentFloor, direction="up"):
  # takes three arguments. requests is a list of floor requests
  while requests:
    if direction == "up":
      requests.sort()
    else: 
      requests.sort(reverse=True)
