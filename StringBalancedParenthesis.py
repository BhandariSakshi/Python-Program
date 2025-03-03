def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)  
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False 
            stack.pop() 

    return not stack  


s = input("Enter the parentheses: ")


if is_balanced(s):
    print("Parentheses are balanced or valid")
else:
    print("Parentheses are not balanced or not valid")
