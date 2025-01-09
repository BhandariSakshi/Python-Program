class StringX:

    def StrCatX(self, Arr,Brr):

        #return Arr+Brr
        Result = []

        for char in Arr:
            Result.append(char)

        for char in Brr:
            Result.append(char)

        Str = ''.join(Result)

        return Str


def main():

    Arr = input("Enter the first string: ")

    Brr = input("Enter the second string: ")

    obj = StringX()

    Result = obj.StrCatX(Arr, Brr)
    print(Result)

if __name__ == "__main__":
    main()