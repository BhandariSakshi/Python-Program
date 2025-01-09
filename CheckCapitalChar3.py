class Charecter:

    def Check(self, ch):
        if ch >= 'A' and ch <= 'Z':
            return True
        else:
            return False

def main():
    ch = input("Enter the charecter: ")

    obj = Charecter()
    bRet = obj.Check(ch)

    if bRet is True:
        print("It is capital letter")

    else:
         print("It is not capital letter")

if __name__ == "__main__":
    main()
