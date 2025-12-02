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
    for line in file.readlines():
        print(line, end='') 



# Test print
print(f"The dial is rotated {direction} {distance} times and points at {currentValue}")
