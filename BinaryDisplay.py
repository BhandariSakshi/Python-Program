class Number:

    def Display(self, iNo):

        iDigit = 0
        Binary = []
        while iNo != 0:

            iDigit = iNo % 2
            Binary.append(iDigit)
            iNo = iNo // 2

        for i in Binary:
            print(i,end=" ")

def main():

    iValue = int(input("Enter the number: "))

    obj = Number()
    obj.Display(iValue)

if __name__ == "__main__":
    main()