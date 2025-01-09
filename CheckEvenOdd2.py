def evenOdd(iValue):
    if iValue % 2 == 0:
        return True
    
        
iNo = int(input("Enter the number: "))

bRet = evenOdd(iNo)

if bRet == True:
    print("It is even number")
else:
    print("It is odd number")  