
from sys import stdin

testing = False
if not testing:
    n_tests = int(stdin.readline())
else:
    n_tests = 1
    
    
def number_of_combos(length, bricks, cache):
    
    combos = 0
    
    for brick in bricks:
        
        
        if (diff:=length - brick) > 0:
            if diff not in cache:
                cache[diff] = number_of_combos(diff, bricks, cache)
            
            combos += cache[diff]
            
        elif diff == 0:
            combos += 1
            
       
       
            
            
    return combos
            
            

for i in range(n_tests):
    if not testing:
        length = int(stdin.readline().split(' ')[1])
        bricks = sorted([int(n) for n in stdin.readline().split()])
    else:
        length, bricks = 5, [int(n) for n in "1 2".split()] # 8
        length, bricks = 7, [int(n) for n in "1 3".split()] # 9
        # length, bricks = 5, [int(n) for n in "1 1 1 1 1".split()] # 3125
        # length, bricks = 10, [int(n) for n in "1 1 2 2".split()]
        length, bricks = 10000, [int(n) for n in "1 17 91 101 336 775 1001 2345 2468 7777".split()]
        
    bricks.reverse()
    
    cache = {0:0}
    
    combos = 0
    for brick in bricks:
        if (diff:=length - brick) > 0:
            if diff not in cache:
                cache[diff] = number_of_combos(diff, bricks, cache)
            
            combos += cache[diff]
            
        elif diff == 0:
            combos += 1
        
    
    print(combos % 1000000009)
    # print(number_of_combos(length, bricks, cache) % 1000000009)