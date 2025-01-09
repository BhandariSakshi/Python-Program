class Charecter:

    def Check(self, ch):
        bFlag = False
        if ch >= 'A' and ch <= 'Z':
            bFlag = True
        
        return bFlag
        

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
