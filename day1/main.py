# when turning left, number DEcreases
# when turning right, number INcreases
# Turning left from zero cycles to 99
# Start value is 50

startInt = 50
direction = "left"
distance = 0
currentValue = startInt

with open("example.txt", 'r') as file:
    #file processing
    listGuide = file.readlines()
    print(f"Working list: {listGuide}")
    for direction in listGuide:
        #print(f"Currently facing: {direction[0]}")
        if direction[0] == 'L':
            print(f"LEFT: {direction[0]}, {direction[1:]}")
        elif direction[0] == 'R':
            print(f"RIGHT: {direction[0]}, {direction[1:]}")

# Test print
#print(f"The dial is rotated {direction} {distance} times and points at {currentValue}")
