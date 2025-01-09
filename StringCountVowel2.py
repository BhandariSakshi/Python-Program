class Strings:

    def CountVowel(self, Arr):
        iCount = 0

        for i in Arr:
            if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                iCount += 1

        return iCount
    
def main():

    Str = input("Enter the string: ")

    obj = Strings()
    iRet = obj.CountVowel(Str)
    print("Number of vowels are: ",iRet)

if __name__ == "__main__":
    main()