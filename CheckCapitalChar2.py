class Charecter:

    def Check(self, ch):
        if ch.isupper:
            print("It is capital letter")
        else:
            print("It is not capital letter")

ch = input("Enter the charecter: ")

obj = Charecter()
obj.Check(ch)