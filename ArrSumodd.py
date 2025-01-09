def Sum(Arr):
    i = 0
    iSum = 0
    for i in range(0, len(Arr)):
        if Arr[i] % 2 != 0:
            iSum = iSum + Arr[i]

    return iSum

Arr = [10, 20, 11, 17, 56]
iRet = Sum(Arr)
print("Sum of odd elements is: ",iRet)