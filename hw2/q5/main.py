from sys import stdin

line = stdin.readline().split(" ")
K = int(line[0])
H = int(line[1])

result = 0
j = 0

while result + K * 2 ** j < H:
    result += K * 2 ** j
    j += 1

print(H - result)