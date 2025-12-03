# when turning left, number DEcreases
# when turning right, number INcreases
# Turning left from zero cycles to 99
# Start value is 50

startInt = 50

with open("input.txt", 'r') as file:
    #file processing
    currentValue = startInt
    zeroTally = 0
    listGuide = file.readlines()
    #print(f"Working list: {listGuide}")

    
    for direction in listGuide:
        #print(f"Currently pointing at {currentValue}")
        if direction[0] == 'L':
            #print(f"LEFT: {direction[0]}, {direction[1:]}")
            distance = int(direction[1:])
            print(f"Rotated Left {distance}")
            while distance > 0:
                if currentValue <= 0:
                    currentValue = 99
                    #print("Turning dial to 99")
                else:
                    currentValue -= 1
                    #print(f"Current value pointing at {currentValue}")
                distance -= 1
            print(f"to point at {currentValue}")
            print("---------------------------")
            
            
        elif direction[0] == 'R':
            #print(f"RIGHT: {direction[0]}, {direction[1:]}")
            distance = int(direction[1:])
            print(f"Rotated Right {distance}")
            while distance > 0:
                if currentValue >= 99:
                    currentValue = 0
                    #print("Turning dial to 0")
                else:
                    currentValue += 1
                distance -= 1
            print(f"to point at {currentValue}")
            print("---------------------------")
            
                
        else:
            print(" No L or R found!")
        if currentValue == 0:
            zeroTally += 1
    print(f"Password: {zeroTally}")

# Test print
#print(f"The dial is rotated {direction} {distance} times and points at {currentValue}")
