class Strings:

    def CountSmall(self, Arr):

        iCount = 0
        for i in Arr:
            if i >= 'a' and i <= 'z':
                iCount += 1

        return iCount
    
def main():

    Str = input("Enter the string: ")

    obj = Strings()
    iRet = obj.CountSmall(Str)
    print("Number of small letters are: ",iRet)

if __name__ == "__main__":
    main()