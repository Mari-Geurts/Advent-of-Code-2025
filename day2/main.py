"""
### To fucking do list ###
- grab first id and last id [CHECK]
- turn firstID and lastID into a range [CHECK]
- Increment through the range [CHECK]
- invalid ids are when the range has repeated digits. ie `55` `6464` and `123123` [CHECK]
- Invalid IDs now include any repeated patterns, find even length first [CHECK]
 - Find odd length Invalid IDs [ ]
- Find all invalid ids and add them up. [ ]
"""
import re

with open("testInput.txt", "r") as file:

    document = file.readline().rstrip()
    listIds = re.split("[-,]" ,document)
    invalidSum = 0
    isFirstId = True

    for idRange in listIds:
        
        if isFirstId == True: #determines if it's the firstId
            firstId = int(idRange)
            isFirstId = False

        else: #if not firstId, must be last
            lastId = int(idRange)
            workingRange = range(firstId,lastId+1)
            isFirstId = True
            
            for workingId in workingRange: #determine here if the id is invalid or not       
                indexLength = len(str(workingId))
                half = int(indexLength//2)
                
                for i in range(0,half): # Meaning we stop at the end of the length
                    
                    if indexLength % 2 == 0: # Indicates even amount of characters Not all are invalid. 
                        #We have to determine by splitting down the middle and checking if they're == 
                        workingVarSlice = []  

                        if str(workingId)[:half-i] == str(workingId)[half+i:]: # matches

                            for n in range(0,indexLength,half-i):
                                workingVarSlice.append(str(workingId)[n:n+half-i])
                        
                            for chunk in workingVarSlice:
                                
                                if chunk == workingVarSlice[0]:
                                    isInvalid = True
                                
                                else:
                                    isInvalid = False
                                    break
                            if isInvalid:
                                print(f"Current value invalid, adding {workingId}.")
                                invalidSum+=workingId
                    
                    else: #must be odd length, proceed another method to check if invalid
                        divideBy = indexLength-1

                        while divideBy > 1:
                            if indexLength % divideBy == 0:
                                print(f"No denominator: {divideBy}")
                                
                                #createWorkingVarslice based on divideBy
                            else:
                                pass
                            divideBy -=1
                                    
                
    #print(f"Final sum is {invalidSum}")


