class Strings:

    def Update(self, Str):

        for i in Str:
            for j in i:

                print(j)
           
def main():

    Arr = input("Enter the String: ")

    obj = Strings()

    obj.Update(Arr)

if __name__ == "__main__":
    main()