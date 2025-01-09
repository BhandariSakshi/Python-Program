class Solution:

    def Update(self, iNo):

        iMask = 0xffff7fff
        
        iResult = iNo & iMask

        return iResult

def main():

    iValue = int(input("Enter the number: "))

    obj = Solution()

    iRet = obj.Update(iValue)
    
    print("Updated umber is: ",iRet)

if __name__ == "__main__":
    main()