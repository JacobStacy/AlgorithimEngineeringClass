from sys import stdin
import math

min = 0
# max = int(stdin.readline().split(" ")[0]) - 1
max = 19

curr_pos = min + math.ceil((max - min) / 2)
# for line in stdin.readline().split(" "):
for line in "13 1 11 10 6".split(" "):
    new_guard = int(line)
    
    if new_guard > max or new_guard < min:
        continue
    
    if new_guard >= curr_pos:
        max = new_guard
    else:
        min = new_guard
    
    curr_pos = min + math.ceil((max - min) / 2)
    print(min, curr_pos, max)
    
print(max - curr_pos)
        
    
    
