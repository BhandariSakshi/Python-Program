class Pattern:

    def Display(self):
        i = 0
        j = 0
        for i in range(0,3):
            for j in range(0,4):
                print("*\t",end=" ")

            print()

obj = Pattern()
obj.Display()