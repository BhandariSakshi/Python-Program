class StringX:

    def StrCmpX(self, Arr,Brr):

        if len(Arr) != len(Brr):
            return False
        
        for i in range(0,len(Arr)):
            if Arr[i] == Brr[i] and len(Arr) == len(Brr):
                return True

def main():

    Arr = input("Enter the first string: ")

    Brr = input("Enter the second string: ")

    obj = StringX()

    Result = obj.StrCmpX(Arr, Brr)

    if Result == True:
        print("Strings are identical")
    else:
        print("Stringa are not identical")
    

if __name__ == "__main__":
    main()