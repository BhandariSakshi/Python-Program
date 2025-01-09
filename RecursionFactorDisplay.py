class Recursion:

    def Display(self,iNo,i):

        if i <= (iNo/2):
            if iNo % i == 0:
                print(i)
            
            self.Display(iNo,i+1)
            

def main():

    iValue = int(input("Enter the number: "))

    obj = Recursion()
    obj.Display(iValue,1)


if __name__ == "__main__":
    main()