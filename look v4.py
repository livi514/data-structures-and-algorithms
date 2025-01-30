def input_file():
    file = {}
    with open("input.txt") as f:
        for line in f:
            (floor, request) = line.split(":")
            file[floor] = request
            print(file)
