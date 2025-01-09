def Count(Arr, iValue):
    i = 0
    iFrequency = 0
    for i in range(0, len(Arr)):
        if Arr[i] == iValue:
            iFrequency = iFrequency+1

    return iFrequency
    

Arr = [10, 23, 65, 65, 28]

iValue = int(input("Enter the number of which you want to find frequency: "))

iRet = Count(Arr,iValue)
print(iValue, " is present ", iRet," times")
    