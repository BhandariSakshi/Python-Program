import math

class FahToCel:

    def convert(self, Start, End, Step):
        cel = 0.0
        i = 0.0

        while Start <= End:
            cel = (5.0/9.0)*(Start-32)

            if cel >= 0:
                print(Start,"\t",math.floor(cel))

            else:
                print(Start,"\t",math.ceil(cel))

            Start += Step

def main():

    fStart = float(input("Enter the starting point of Fahrenheit: "))
    fEnd = float(input("Enter the ending point of fahrenheit:  "))
    fStep = float(input("Enter the steps to be taken: "))

    obj = FahToCel()
    obj.convert(fStart, fEnd, fStep)


if __name__ == "__main__":
    main()