class Strings:

    def CountSpaces(self, Arr):
        iCount = 0

        for i in Arr:
            if i == ' ':
                iCount += 1
        
        return iCount

def main():

    Arr = input("Enter the string: ")

    obj = Strings()

    iRet = obj.CountSpaces(Arr)
    print("Number of spaces: ", iRet)

if __name__ == "__main__":
    main()