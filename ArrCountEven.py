def Count(Arr):
    i = 0
    iCount = 0
    for i in range(0, len(Arr)):
        if Arr[i] % 2 == 0:
            iCount = iCount + 1

    return iCount

Arr = [10, 20, 11, 17, 56]
iRet = Count(Arr)
print("Number of even elements are: ",iRet)