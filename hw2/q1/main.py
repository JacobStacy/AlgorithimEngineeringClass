from sys import stdin
import heapq

capacity = int(stdin.readline().split(" ")[1])

infestations = []
for line in stdin.readlines():
    heapq.heappush(infestations, -int(line))

for i in range(capacity):
    print(-heapq.heappop(infestations))