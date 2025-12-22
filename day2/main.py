"""
### To fucking do list ###
- grab first id and last id [CHECK]
- turn firstID and lastID into a range [CHECK]
- Increment through the range [CHECK]
- invalid ids are when the range has repeated digits. ie `55` `6464` and `123123` [CHECK]
- Invalid IDs now include any repeated patterns, find even length first [CHECK]
- Find odd length Invalid IDs [CHECK]
- Find all invalid ids and add them up. [CHECK]
"""
import re

with open("input.txt", "r") as file:

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
                
                for i in range(0,half): # Meaning we stop at the floor(//) halfway point
                    workingVarSlice = []

                    if indexLength % 2 == 0: # Indicates even amount of characters Not all are invalid. 
                        #We have to determine by splitting down the middle and checking if they're == 
                         

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
                                #print(f"Current value invalid, adding {workingId}.")
                                invalidSum+=workingId
                                break
                        
                    else: #must be odd length, proceed another method to check if invalid
                        #breakpoint()

                        if str(workingId)[:half-i] == str(workingId)[half+i+1:]: # both halves matched

                            for n in range(0,indexLength,half-i): # We iterate through the workingId and append to workingVarSlice
                                
                                workingVarSlice.append(str(workingId)[n:n+half-i])

                            for chunk in workingVarSlice: # for every chunk within the slice

                                if chunk == workingVarSlice[0]: # We check if all chunks are equivalent, makking it invalid
                                    isInvalid = True                                   

                                else: # If they do not match, automatically makes them valid
                                    isInvalid = False
                                    break

                            if isInvalid:
                                #print(f"STEP 5: Current value invalid, adding {workingId}.")
                                invalidSum+=workingId
                                break
                                
                
    print(f"Final sum is {invalidSum}")



# Correct answer 26202168557 !!!