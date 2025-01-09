def Count(Arr, iValue):
    i = 0
    for i in range(0, len(Arr)):
        if Arr[i] == iValue:
            break

    if i == len(Arr):
        return False
    else:
        return True
    

Arr = [10, 23, 65, 65, 28]

iValue = int(input("Enter the number which you want to find: "))

bRet = Count(Arr,iValue)
if bRet == True:
    print(iValue, " is present")

else:
    print(iValue, " is not present")
    