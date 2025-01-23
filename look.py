'''
LOOK algorithm. Like SCAN, but the direction can be changed at any point if no
more requests exist in the current direction
'''

#ground floor - floor number 0

top_floor_number = 10 #value can be any positive integer
number_of_floors = top_floor_number + 1 #top floor number + the ground floor (floor 0)
direction_of_travel = "up" #can be "up" or "down"
current_floor = 0

#example requests - we will need to change the way that requests are processed for the real-time version of the algorithm 
request_list = [6, 2, 8, 7, 5]

#function to handle one lift journey - here, a lift journey will be the lift either travelling upwards or downwards
def lift_journey():
  #I've planned out the algorithm I just need to type it up in python 