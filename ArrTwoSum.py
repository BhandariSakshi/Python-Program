class ArrayX:
    def __init__(self, size):
        print("Inside the constructor")
        self.size = size
        self.arr = [0] * size 

    def accept(self):
        print("Enter the elements: ")
        for i in range(self.size):
            self.arr[i] = int(input())

    def two_sum(self, target):
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                if self.arr[i] + self.arr[j] == target:
                    return (i, j)  
        return None 

def main():
    target = int(input("Enter the target sum: "))
    count = int(input("Enter the number of elements you want to store: "))

    obj = ArrayX(count)  

    obj.accept() 

    result = obj.two_sum(target)  

    if result is not None:
        print(f"Indices: {result[0]} and {result[1]}")
    else:
        print("No two elements found with the given sum.")


if __name__ == "__main__":
    main()
