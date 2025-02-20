class Solution:

    def Sqrt(self, iNum):

        if iNum == 0 or iNum == 1:
            return iNum
        left = 1
        right = iNum
        ans = 0

        while left <= right:
            mid = left+(right-left)//2
            if mid*mid == iNum:
                return mid
            elif mid*mid < iNum:
                ans = mid
                left = mid + 1
            else:
                right = mid-1

        return ans 

def main():

    iValue = int(input("Enter the number: "))

    obj = Solution()
    iRet = obj.Sqrt(iValue)
    print("Answer is: ",iRet)

if __name__ == "__main__":
    main()