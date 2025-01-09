class StringX:

    def StrCpySmallX(self, Src):

        Dest = " "

        for char in Src:
            if char>= 'a' and char <= 'z':
                Dest += char

        return Dest
    
    '''Dest = ''.join(Src)
        return Dest'''
    
def main():

    Arr = input("Enter the source string: ")

    obj = StringX()

    Brr = obj.StrCpySmallX(Arr)
    print("Destination string is: ", Brr)

if __name__ == "__main__":
    main()