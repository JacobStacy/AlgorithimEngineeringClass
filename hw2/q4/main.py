from sys import stdin
import math

min = 0
max = int(stdin.readline())[0] - 1

curr_pos = min + math.ceil((max - min) // 2)
for line in stdin.readlines():
    line = int(line)
    
