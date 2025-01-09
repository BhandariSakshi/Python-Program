class Strings:

    def StrLenX(self, Arr):
        iCount = 0

        for i in Arr:
            iCount += 1

        return iCount

def main():

    Str = input("Enter the string: ")

    obj = Strings()
    iRet = obj.StrLenX(Str)
    print("Length of String is: ",iRet)

if __name__ == "__main__":
    main()