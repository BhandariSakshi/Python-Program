class Strings:

    def Reverse(self, Str):

        char = list(Str)
        Start = 0
        End = len(char)-1

        while Start < End:

            temp = char[Start]
            char[Start] = char[End]
            char[End] = temp

            Start += 1
            End -= 1

        reversed_str = ''.join(char)
        print("Reversed String: ", reversed_str)

def main():

    Arr = input("Enter Strings: ")

    obj = Strings()

    obj.Reverse(Arr)

if __name__ == "__main__":
    main()