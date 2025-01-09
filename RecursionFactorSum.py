class Recursion:

    def Sum(self,iNo,i,iSum):

        if i <= (iNo/2):
            if iNo % i == 0:
                iSum = iSum + i
            
            iSum = self.Sum(iNo,i+1,iSum)

        return iSum
            

def main():

    iValue = int(input("Enter the number: "))

    obj = Recursion()

    iRet = obj.Sum(iValue,1,0)
    print("Sum of factors: ",iRet)


if __name__ == "__main__":
    main()