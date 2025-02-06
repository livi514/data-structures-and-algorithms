def scan_elevator(floors, start, direction, max_floor):
    start = 0 # always start at the bottom?
    # arrange the floors in ascending order
    floors.sort() 
    # Splitting requests into two parts: below and above the current floor
    lower_floors = [floor for floor in floors if floor < start]
    higher_floors = [floor for floor in floors if floor >= start]

    scan_order = []
  
    if direction == 'up':
        # Serve higher floors first, then reverse to lower floors
        scan_order.extend(higher_floors)
        scan_order.extend(reversed(lower_floors))
    else:
        # Serve lower floors first, then reverse to higher floors
        scan_order.extend(reversed(lower_floors))
        scan_order.extend(higher_floors)

    return scan_order
