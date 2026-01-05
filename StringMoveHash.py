def move_hash(s):
    hashes = ""
    others = ""

    for ch in s:
        if ch == '#':
            hashes += ch
        else:
            others += ch

    return hashes + others


# Input
s = input("Enter the string: ")
result = move_hash(s)

print("String after moving hash: ",result)
