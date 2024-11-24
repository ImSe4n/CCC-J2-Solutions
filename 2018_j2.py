n = int(input())
a = list(input())
b = list(input())

count = 0

for i in range(n):
    if a[i] == b[i] and a[i] == 'C':
        count += 1
print(count)