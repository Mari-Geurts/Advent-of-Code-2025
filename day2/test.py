testLength = 10
n = testLength-1
while n > 1:
    if testLength % n == 0:
        print(f"No denominator: {n}")
    else:
        print(testLength % n)
    n -=1
