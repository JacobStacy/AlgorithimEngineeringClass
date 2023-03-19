from sys import stdin

n_tests = int(stdin.readline())
        
def lowest_remaining(remaining, buttons):
    
    lowest = remaining
    
    for i in range(len(buttons)):
        
        if remaining % buttons[i] == 0:
            return 0
        
        if (n:=remaining - buttons[i]) >= 0:
            lowest = l if (l:=lowest_remaining(n, buttons)) < lowest else lowest
        
    return lowest
        


for i in range(n_tests):
    heat_limit = int(stdin.readline().split(' ')[1])
    buttons = [int(n) for n in stdin.readline().split(' ')]
    
    print(heat_limit - lowest_remaining(heat_limit, buttons))