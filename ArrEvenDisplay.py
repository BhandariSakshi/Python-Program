def EvenDisplay(Arr):
    i = 0
    for i in range(0, len(Arr)):
        if Arr[i] % 2 == 0:
            print(Arr[i])

Arr = [11,23,22,55,12]

print("Even numbers are: ")
EvenDisplay(Arr)