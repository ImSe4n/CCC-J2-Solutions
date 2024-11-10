n = int(input())
t = 0
spiceVals = {'Poblano': 1500, 'Mirasol': 6000, 'Serrano': 15500, 'Cayenne': 40000, 'Thai': 75000, 'Habanero': 125000} 

for i in range(n):
    spice = input()
    t += spiceVals[spice]

print(t)