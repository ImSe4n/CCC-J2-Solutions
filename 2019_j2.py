num_lines = int(input())
lines = []
for i in range(num_lines):
    lines.append(input())
for lines in lines:
    values = lines.split()
    print(values[1] * int(values[0]))