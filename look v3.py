'''
LOOK algorithm with input file
'''

import time

#processing the input file 
def process_input_file():
  input_file = open("input.txt")
  input_file.readline() #reads the first line but doesn't do anything with it, as the first line is just a description of the second file 
  floors_and_capacity = input_file.readline().split(",") #gets the second line of the file
  floors = floors_and_capacity[0].strip()
  capacity = floors_and_capacity[1].strip()
  
  
