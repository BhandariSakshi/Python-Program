def Divisible(Arr):
    i = 0
    iCount = 0
    for i in range(0, len(Arr)):
        if Arr[i] % 5 == 0 and Arr[i] % 3 == 0:
            iCount = iCount + 1

    return iCount

Arr = [15, 5, 10, 30, 45]
iRet = Divisible(Arr)
print("Number of elements divisible by 5 and 3: ",iRet)