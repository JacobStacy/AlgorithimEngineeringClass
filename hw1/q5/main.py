import sys

sys.stdin.readline()

for line in sys.stdin:
    
    line = line.split(" ")
    n, m, c = int(line[0]), int(line[1]), int(line[2])
    
    total = n // m
    
    created = total // c
    left_over = total % c
    
    total += created
    
    while left_over + created >= c:
        created, left_over = (left_over + created) // c, (left_over + created) % c
        total += created
    
    print(total)