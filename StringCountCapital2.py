class Strings:

    def CountCapital(self, Arr):

        iCount = 0
        for i in Arr:
            if ord(i) >= 65 and ord(i) <= 90:
                iCount += 1

        return iCount
    
def main():

    Str = input("Enter the string: ")

    obj = Strings()
    iRet = obj.CountCapital(Str)
    print("Number of capital letters are: ",iRet)

if __name__ == "__main__":
    main()