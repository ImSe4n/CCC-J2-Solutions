l = int(input())

for i in range(l):
    count, symbol = input().split()
    print(symbol * int(count))