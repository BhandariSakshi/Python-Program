class Charecter:

    def Check(self, ch):
        bFlag = False
        if ch >= 'a' and ch <= 'z':
            bFlag = True
        
        return bFlag
        

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
