class Charecter:

    def Check(self, ch):
        if ch >= 'a' and ch <= 'z':
            print("It is small letter")
        else:
            print("It is not small letter")

ch = input("Enter the charecter: ")

obj = Charecter()
obj.Check(ch)