class Quadrant:
    def Check(self, x, y):
        if x > 0 and y > 0:
            print("1st quadrant")

        elif x < 0 and y > 0:
            print("2nd quadrant")

        elif x < 0 and y < 0:
            print("3rd quadrant")

        elif x > 0 and y < 0:
            print("4th quadrant")

        elif x == 0 and y == 0:
            print("Origin")

        elif x == 0:
            print("Y axis")

        elif y == 0:
            print("X asix")

x = int(input("Enter the x co-ordinate: "))
y = int(input("Enter the y co-ordinate: "))

obj = Quadrant()
obj.Check(x,y)