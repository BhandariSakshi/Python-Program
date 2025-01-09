class Number:

    def Difference(self, iNo):

        iAns = 0
        iSumF = 0
        iSumN = 0

        for i in range(1, iNo):
            
            if iNo % i == 0:
                iSumF += i

            else:
                iSumN +=  i

        iAns = iSumN - iSumF

        return iAns

def main():

    iValue = int(input("Enter the number: "))

    obj = Number()
    
    iRet = obj.Difference(iValue)
    print("Difference between non factors and factors: ",iRet)
    
if __name__ == "__main__":
    main()