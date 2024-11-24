VALID = "I", "O", "S", "H", "Z", "X", "N"
word = input()

if all(letter in VALID for letter in word):
    print("YES")
else:
    print("NO")