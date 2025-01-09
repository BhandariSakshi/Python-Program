def Sum(Arr):
    iSum = 0
    for i in range(0, len(Arr)):
        iSum += Arr[i]

    return iSum

Arr = [10,20,30,40]

iRet = Sum(Arr)

print("Sum is: ", iRet)