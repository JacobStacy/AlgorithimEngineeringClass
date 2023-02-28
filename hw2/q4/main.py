from sys import stdin

min = 0
max = int(stdin.readline().split(" ")[0]) - 1

guards = []

for line in stdin.readline().split(" "):
    guards.append(int(line))
        
guards.sort()

max_dist = 0
for i in range(1, len(guards)):
    dist = guards[i] - guards[i - 1]
    
    if dist == 1: 
        dist -= 1
        
    dist = dist // 2 
        
    if max_dist < dist:
        max_dist = dist

if guards[0] - min > max_dist:
    max_dist = guards[0] - min

if max - guards[-1] > max_dist:
    max_dist = max - guards[-1]

print(max_dist)