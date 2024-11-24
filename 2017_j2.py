n = int(input())
k = int(input())

count = 0
shifts = 0

while shifts <= k:
    count += n * 10 ** shifts
    shifts += 1
print(count)