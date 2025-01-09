def Display(iNo):

    if iNo > 0:
        print(iNo%10)
        iNo = iNo // 10
        Display(iNo)

def main():

    iValue = int(input("Enter the number: "))

    Display(iValue)

if __name__ == "__main__":
    main()