class Charecter:

    def Check(self, ch):
        if ch >= 'a' and ch <= 'z':
            return True
        else:
            return False

def main():
    ch = input("Enter the charecter: ")

    obj = Charecter()
    bRet = obj.Check(ch)

    if bRet is True:
        print("It is small letter")

    else:
         print("It is not small letter")

if __name__ == "__main__":
    main()
