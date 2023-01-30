import sys

sys.stdin.readline()

for line in sys.stdin:
# for line in ["6 12", "25 37"]:
    
    line = line.split(" ")
    x, y = int(line[0]), int(line[1])
    
    num_divisible = 0 # Every 12
    num_square = 0 # sqrt rounded up
    num_both = 0 #dont know yet
    
    #brute force
    for i in range(x, y + 1):
        
        divisible = i % 12 == 0
        square = int(i ** .5) ** 2 == i
        
        if divisible:
            num_divisible += 1
        if square:
            num_square += 1
        if divisible and square:
            num_both += 1
        
        
            
    print(num_divisible, num_square, num_both)
            
            
            
    