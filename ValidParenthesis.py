class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (ch == ')' and top != '(') or \
                   (ch == '}' and top != '{') or \
                   (ch == ']' and top != '['):
                    return False

        return len(stack) == 0

# Main block
if __name__ == "__main__":
    input_str = input("Enter the string: ")
    obj = ValidParenthesis()

    if obj.isValid(input_str):
        print("Valid Parenthesis")
    else:
        print("Not Valid Parenthesis")
