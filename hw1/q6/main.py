import sys
import math

sys.stdin.readline()

for line in sys.stdin:
    
    line = line.split(" ")
    x, y = int(line[0]), int(line[1])
    
    divisible = 0 # Every 12
    square = 0 # sqrt rounded up
    both = 0 #dont know yet

    # Handle if divisible by 12
    if x % 12 == 0:
        divisible += 1
    
    next_twelve = x + (12 - (x % 12))
    if y >= next_twelve:
        divisible += ((y - next_twelve) // 12) + 1
        
    # Handle perfect square
    if int(x ** .5) ** 2 == x:
        square += 1
        
    start = int(x ** .5)
    end = int(y ** .5)
    
    square += (end - start)
    
    # Handle both
    if int(x ** .5) ** 2 == x and x % 12 == 0:
        both += 1
    
    next_six = start + (6 - (start % 6))
    if end >= next_six:
        both += ((end - next_six) // 6) + 1
    
    print(divisible, square, both)
            
            
            
    