from sys import stdin

k_stabalizers = int(stdin.readline().split(" ")[1])
costs = sorted([int(i) for i in stdin.readline().split(" ")], reverse=True)

total = 0
for i in range(len(costs)):
    total += costs[i] * ((i // k_stabalizers) + 1)

print(total)