var1 = "2121212121"
var2 = "565656"
var3 = "824824824"
var4 = "1234567890"

strWorkingVar = var1
totalSum = 0

indexLength = len(strWorkingVar)
half = indexLength//2
leftHalf = strWorkingVar[:int(indexLength//2)]
rightHalf = strWorkingVar[int(indexLength//2):]

#-----------
if indexLength % 2 == 0: #check length is even

    for i in range(0,half): # Meaning we stop at the end of the length
        workingVarSlice = []
        if strWorkingVar[:half-i] == strWorkingVar[half+i:]: # matches
            x = 0
            for n in range(0,indexLength,half-i):
                workingVarSlice.append(strWorkingVar[n:n+half-i])
                #print(f"{n} | values i: {i} | indexLength: {indexLength} | half-i: {half-i}")
                #print(workingVarSlice)
                
                for chunk in workingVarSlice:
                    #print(chunk)
                    
                    if chunk == workingVarSlice[0]:
                        print(f"{workingVarSlice[0]} matches {chunk} | Moving on...")
                        x+=1
                    
                    else:
                        print(f" {workingVarSlice[0]} does NOT match {chunk} | Breaking cycle")
                        break
                        
            
        else: # doesn't match
            pass
            #print(f"Left: {strWorkingVar[:half-i]} does NOT match Right: {strWorkingVar[half+i:]}")
                
print(f"Total sum: {totalSum}")

"""testLength = 10
n = testLength-1
while n > 1:
    if testLength % n == 0:
        print(f"No denominator: {n}")
    else:
        print(testLength % n)
    n -=1
"""
