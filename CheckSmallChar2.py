class Charecter:

    def Check(self, ch):
        if ch.islower:
            print("It is small letter")
        else:
            print("It is not small letter")

ch = input("Enter the charecter: ")

obj = Charecter()
obj.Check(ch)