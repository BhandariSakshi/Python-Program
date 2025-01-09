class StringX:

    def StringToggleX(self, Arr):

        Str = []
        for i in Arr:

            if i >= 'a' and i <= 'z':
                Str.append(chr(ord(i) - 32))
            elif i >= 'A' and i <= 'Z':
                Str.append(chr(ord(i) + 32))

        return ''.join(Str)

def main():

    Arr = input("Enter the string: ")

    obj = StringX()

    sRet = obj.StringToggleX(Arr)
    print("Update string is: ",sRet)

if __name__ == "__main__":
    main()