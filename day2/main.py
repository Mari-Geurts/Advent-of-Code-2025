#To fucking do list
# grab first id and last id [CHECK]
# turn firstID and lastID into a range [CHECK]
# Increment through the range [CHECK]
# invalid ids are when the range has repeated digits. ie `55` `6464` and `123123` [CHECK]
#Find all invalid ids, and add them up. [CHECK]
import re

with open("input.txt", "r") as file:
    #file processing

    document = file.readline().rstrip()
    listIds = re.split("[-,]" ,document)
    invalidSum = 0
    counter = 1

    for idRange in listIds:
        
        if counter == 1: #determines if it's the firstId
            firstId = int(idRange)
            counter += 1

        else: #if not firstId, must be last
            lastId = int(idRange)
            workingRange = range(firstId,lastId+1)
            
            for i in workingRange: #determine here if the id is invalid or not       
                indexLength = len(str(i))
                half = int(indexLength//2)

                if indexLength % 2 == 0: # Indicates that there is an even amount of characters, Not all are invalid; we have to determine by splitting down the middle and checking if they're == 

                    if str(i)[:half] == str(i)[half:]: # If first half and last half match, then they are invalid
                        #print(f"{i} is {indexLength} long. It begins with {str(i)[:int(indexLength//2)]} and ends with {str(i)[int(indexLength//2):]}")
                        invalidSum += i

                    else: #if left half != right half, proceed another method to check if invalid
                        
                        pass    

                else: #must be odd value, proceed another method to check if invalid
                    
                    pass
                
            counter = 1
    print(f"Final sum is {invalidSum}")

