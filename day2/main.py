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
                
                for i in range(0,half): # Meaning we stop at the floor(//) halfway point
                    workingVarSlice = []

                    if indexLength % 2 == 0: # Indicates even amount of characters Not all are invalid. 
                        #We have to determine by splitting down the middle and checking if they're == 
                         

                        if str(workingId)[:half-i] == str(workingId)[half+i:]: # matches
                            """print("                       ")
                            print(f"STEP 1: If {str(workingId)[:half-i]} equals {str(workingId)[half+i:]} then we proceed")
                            print("- - - - - - - - - - - -")"""
                            
                            for n in range(0,indexLength,half-i): 
                                """print("                       ")
                                print(f"STEP 2: for {n} in range(0,{indexLength},{half-i})")
                                print(f"We append {str(workingId)[n:n+half-i]} to the list {workingVarSlice}")
                                print("- - - - - - - - - - - -")"""

                                workingVarSlice.append(str(workingId)[n:n+half-i])
                        
                            for chunk in workingVarSlice:
                                """print("                       ")
                                print(f"STEP 3: for chunk `{chunk}` in {workingVarSlice}")
                                print("- - - - - - - - - - - -")"""
                                

                                if chunk == workingVarSlice[0]:
                                    isInvalid = True
                                    """print("                       ")
                                    print(f"STEP 4: if {chunk} is equal to the start of our list {workingVarSlice[0]}")
                                    print(f"We set isInvalid to {isInvalid}")
                                    print("- - - - - - - - - - - -")"""
                                    
                                
                                else:
                                    isInvalid = False
                                    break

                            if isInvalid:
                                print(f"Current value invalid, adding {workingId}.")
                                invalidSum+=workingId
                                break
                        
                    else: #must be odd length, proceed another method to check if invalid
                        breakpoint()
                        if str(workingId)[:half-i+1] == str(workingId)[half+i:]: # both halves matched
                            
                            """
                            print(f"STEP 1: If {str(workingId)[:half-i+1]} equals {str(workingId)[half+i:]} then we proceed")
                            print("                       ")
                            print("- - - - - - - - - - - -")"""
                            for n in range(0,indexLength,half-i+1): # We iterate through the workingId and append to workingVarSlice
                                """
                                print("                       ")
                                print(f"STEP 2: for {n} in range(0,{indexLength},{half-i+1})")
                                print(f"We append {str(workingId)[n:n+half-i+1]} to the list {workingVarSlice}")
                                print("- - - - - - - - - - - -")"""

                                workingVarSlice.append(str(workingId)[n:n+half-i+1])

                                for chunk in workingVarSlice: # for every chunk within the slice
                                    """
                                    print(f"STEP 3: for chunk `{chunk}` in {workingVarSlice}")
                                    print("                       ")
                                    print("- - - - - - - - - - - -")"""

                                    if chunk == workingVarSlice[0]: # We check if all chunks are equivalent, makking it invalid
                                        isInvalid = True
                                        """
                                        print(f"STEP 4: if {chunk} is equal to the start of our list {workingVarSlice[0]}")
                                        print(f"We set isInvalid to {isInvalid}")
                                        print("                       ")
                                        print("- - - - - - - - - - - -")"""
                                        

                                    else: # If they do not match, automatically makes them valid
                                        isInvalid = False
                                        print(f"WorkingId is valid: {workingId}")
                                        break
                                        
                                    
                            if isInvalid:
                                print(f"Current value invalid, adding {workingId}.")
                                invalidSum+=workingId
                                break
                                    
                
    print(f"Final sum is {invalidSum}")
    print("                       ")
    print("- - - - - - - - - - - -")

# 854481776553 is too high

# 26190820675 is too low