n = int(input())

f = 0
p = 0
s = 0

for i in range(n):
    p = int(input())
    f = int(input())

    totals = (p*5) - (f*3)
    
    if totals > 40:
        s += 1
    
if s == n:
    print(str(s)+"+")
else:
    print(s)