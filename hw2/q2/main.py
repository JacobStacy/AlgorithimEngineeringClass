from sys import stdin
import heapq

stdin.readline()

stack = []
max_nums = []
in_stack = {}
for line in stdin.readlines():
    
    line =  line.split(" ")
    action = int(line[0])
    
    match action:
        case 1:
            value = int(line[1])
            
            stack.append(value)
            heapq.heappush(max_nums, -value)
            
            if value not in in_stack:
                in_stack[value] = 1
            else:
                in_stack[value] += 1  
                                
        case 2:
            in_stack[stack.pop()] -= 1
            
        case 3:
            while in_stack[-max_nums[0]] == 0:
                heapq.heappop(max_nums)
            print (-max_nums[0])
                
                    
            
        
            
            



        