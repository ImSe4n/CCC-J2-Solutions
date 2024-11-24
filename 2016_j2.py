a = input().split()
b = input().split()
c = input().split()
d = input().split()
    
if int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) == int(b[0]) + int(b[1]) + int(b[2]) + int(b[3]) == int(c[0]) + int(c[1]) + int(c[2]) + int(c[3]) == int(d[0]) + int(d[1]) + int(d[2]) + int(d[3]) == int(a[0]) + int(b[0]) + int(c[0]) + int(d[0]) == int(a[1]) + int(b[1]) + int(c[1]) + int(d[1]) == int(a[2]) + int(b[2]) + int(c[2]) + int(d[2]) == int(a[3]) + int(b[3]) + int(c[3]) + int(d[3]):
    print("magic")
else:
    print("not magic")