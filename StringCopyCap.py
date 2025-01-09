class StringX:

    def StrCpyCapX(self, Src):

        Dest = " "

        for char in Src:
            if char>= 'A' and char <= 'Z':
                Dest += char

        return Dest
    
    '''Dest = ''.join(Src)
        return Dest'''
    
def main():

    Arr = input("Enter the source string: ")

    obj = StringX()

    Brr = obj.StrCpyCapX(Arr)
    print("Destination string is: ", Brr)

if __name__ == "__main__":
    main()