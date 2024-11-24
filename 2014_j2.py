v = int(input())
c = list(input())

num_a = c.count('A')
num_b = c.count('B')

if num_a > num_b:
    print('A')
elif num_a < num_b:
    print('B')
else:
    print('Tie')