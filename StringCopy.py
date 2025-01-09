class StringX:

    def StrCpyX(self, Src):

        Dest = " "

        for char in Src:
            Dest += char

        return Dest
    
    '''Dest = ''.join(Src)
        return Dest'''
    
def main():

    Arr = input("Enter the source string: ")

    obj = StringX()

    Brr = obj.StrCpyX(Arr)
    print("Destination string is: ", Brr)

if __name__ == "__main__":
    main()