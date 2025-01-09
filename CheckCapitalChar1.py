class Charecter:

    def Check(self, ch):
        if ch >= 'A' and ch <= 'Z':
            print("It is capital letter")
        else:
            print("It is not capital letter")

ch = input("Enter the charecter: ")

obj = Charecter()
obj.Check(ch)