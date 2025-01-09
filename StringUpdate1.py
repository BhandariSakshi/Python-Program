class Strings:

    def Update(self, Str):

        s = ''

        for i in Str:
            if i == ' ':
                s += '*'

            else:
                s += i
                
        self.Display(s)

    def Display(self, Str):
        print(Str)

def main():

    Arr = input("Enter the String: ")

    obj = Strings()

    obj.Update(Arr)

if __name__ == "__main__":
    main()