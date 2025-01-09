def Count(Arr, iValue):
    i = 0
    bFlag = False
    for i in range(0, len(Arr)):
        if Arr[i] == iValue:
            bFlag = True
            break

    return bFlag
    

Arr = [10, 23, 65, 65, 28]

iValue = int(input("Enter the number which you want to find: "))

bRet = Count(Arr,iValue)
if bRet == True:
    print(iValue, " is present")

else:
    print(iValue, " is not present")
    