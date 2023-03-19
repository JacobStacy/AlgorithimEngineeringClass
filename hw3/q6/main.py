from sys import stdin
n_tests = int(stdin.readline())

for i in range(n_tests):
    
    remaining, goal = [int(i) for i in stdin.readline().split(' ')]
    
    diff = remaining - goal
    days = 0
    while diff > 0:
        days += diff & 1
        diff >>= 1
        
    print(days)