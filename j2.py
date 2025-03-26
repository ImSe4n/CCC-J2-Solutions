d = int(input())
e = int(input())

for i in range(e):
    operation = input()
    quantity = int(input())
    
    if operation == '+':
        d += quantity
    elif operation == '-':
        d -= quantity

print(d)