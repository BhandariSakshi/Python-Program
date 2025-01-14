def find_max_word(input_string):
    words = input_string.split() 
    max_word = max(words, key=len)  
    return max_word, len(max_word)

def main():

    input_string = input("Enter the string: ")
    max_word, max_length = find_max_word(input_string)

    print(f"The longest word is: {max_word}")
    print(f"Its length is: {max_length}")


if __name__ == "__main__":
   main()