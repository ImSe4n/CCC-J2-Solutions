p = int(input())
n = int(input())
r = int(input())

infected = n
infected_total = n
day = 0

while infected_total <= p:
    infected = infected * r
    infected_total += infected
    day += 1
print(day)