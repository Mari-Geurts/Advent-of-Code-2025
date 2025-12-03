startInt = 50

with open("example.txt", 'r') as file:
    #file processing
    currentValue = startInt
    zeroTally = 0
    listGuide = file.readlines()
    
    for direction in listGuide:

        if direction[0] == 'L':
            distance = int(direction[1:])
            print(f"Rotated Left {distance}")

            while distance > 0:
                if currentValue <= 0:
                    currentValue = 99

                else:
                    currentValue -= 1
                
                distance -= 1
            
        elif direction[0] == 'R':

            distance = int(direction[1:])
            print(f"Rotated Right {distance}")
            
            while distance > 0:
                if currentValue >= 99:
                    currentValue = 0
                    #print("Turning dial to 0")
                else:
                    currentValue += 1
                distance -= 1
                
        else:
            print(" No L or R found!")
        if currentValue == 0:
            zeroTally += 1
    print(f"Password: {zeroTally}")


