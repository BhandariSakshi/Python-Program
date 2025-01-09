class Solution:

    def Power(self, iNo, Pow):

        ans = 1
        binForm = Pow

        if Pow == 0:
            return 1
        if iNo == 1:
            return 1
        if iNo == 0:
            return 0
        if iNo == -1 and Pow%2 == 0:
            return 1
        if iNo == -1 and Pow%2 != 0:
            return -1
        
        if Pow < 0:
            iNo = 1 / iNo
            binForm = -binForm

        while binForm > 0:
            if binForm % 2 == 1:
                ans *= iNo

            iNo *= iNo
            binForm //= 2

        return ans



def main():

    dValue = int(input("Enter the number: "))
    iPower = int(input("Enter the power: "))

    obj = Solution()

    iRet = obj.Power(dValue, iPower)
    print("Answer is: ",iRet)


if __name__ == "__main__":
    main()