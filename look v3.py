'''
LOOK algorithm with input file
'''

import time

#processing the input file 
def process_input_file():
  input_file = open("input.txt", "r")
  input_file.readline() #reads the first line but doesn't do anything with it, as the first line is just a description of the second file 
  floors_and_capacity = input_file.readline().strip().split(",") #gets the second line of the file
  floors = int(floors_and_capacity[0].strip())
  capacity = int(floors_and_capacity[1].strip())
  input_file.readline() #reading the third line
  floor_requests = {}
  for line in input_file:
    floor_and_requests = line.split(":")
    floor = floor_and_requests[0]
    requests = floor_and_requests[1]
    floor_requests[floor] = requests
  print(floor_requests)

process_input_file()
