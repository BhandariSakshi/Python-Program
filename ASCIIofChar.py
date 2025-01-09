class Charecter:

    def Display(self, ch):
        print("Entered charecter is: ",ch)
        print("ASCII of charecter: ",ord(ch))

ch = input("Enter the charecter: ")

obj = Charecter()
obj.Display(ch)