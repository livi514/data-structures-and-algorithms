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
top_floor_reached = false

#lift will start on the ground floor?
bottom_floor_reached = true

