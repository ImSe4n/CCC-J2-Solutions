n = int(input())
max_bid = 0

for i in range(n):
    name = input()
    bids = int(input())
    if bids > max_bid:
        max_bid = bids
        winner = name
print(winner)
