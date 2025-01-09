def display(number):
    print(f"Decimal number: {number}")
    print(f"Octal number: {oct(number)[2:]}")
    print(f"Hexadecimal number: {hex(number)[2:]}")

def main():
    value = int(input("Enter the number: "))
    display(value)

if __name__ == "__main__":
    main()
