# This code is gross

import sys
import copy

class Cross:
    x = -1
    y = -1
    
    size = -1
    
    collision_map = []
    
    processors = 0
    
    def __init__(self, x = -1, y = -1, size = -1):
        self.x = x
        self.y = y
        self.size = size
        
        if size >= 0:
            self.processors = 1 + (size * 4)
        else:
            self.processors = 0
        
    def __lt__(self, other):
        return (self.size < other.size)    
    
    def __eq__(self, other):
        return (self.size == other.size)
    
    def __le__(self, other):
        return self.size < other.size or self.size == other.size
    
    def __str__(self):
        out = ""
        for line in self.collision_map:
            out = out + str(line) + "\n"
        return out
    
    
def find_crosses(lines, marker):
    crosses = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            
            if lines[y][x] == 'B':
                continue
            if x == 4 and y == 3:
                pass
            size = 0
            while 1:
                
                check_y = y - size >= 0 and y + size < len(lines)
                check_x = x - size >= 0 and x + size < len(lines[0])
                
                if check_y and check_x:
                    
                    check_top = lines[y - size][x] == 'G'
                    check_bottom = lines[y + size][x] == 'G'
                    check_left = lines[y][x - size] == 'G'
                    check_right = lines[y][x + size] == 'G'
                    
                    if check_top and check_bottom and check_left and check_right:
                        cross = Cross(x,y,size)
                        copy_lines = copy.deepcopy(lines)
                        for i in range(cross.size + 1):
                            copy_lines[cross.y + i][cross.x] = marker
                            copy_lines[cross.y - i][cross.x] = marker
                            copy_lines[cross.y][cross.x + i] = marker
                            copy_lines[cross.y][cross.x - i] = marker
                        cross.collision_map = copy_lines
                        crosses.append(cross)
                        size += 1
                    else:
                        break
                else:
                    break
                
    return sorted(crosses)

def collided(cross1, cross2):
    x = cross2.x
    y = cross2.y
    
    lines = cross1.collision_map
    
    size = 0
    while size <= cross2.size:
            
        check_top = lines[y-size][x] == 'G'
        check_bottom = lines[y+size][x] == 'G'
        check_left = lines[y][x-size] == 'G'
        check_right = lines[y][x+size] == 'G'
        
        if check_top and check_bottom and check_left and check_right:
            size += 1
            continue
        else:
            return True
    return False

lines = []
sys.stdin.readline()
for line in sys.stdin:
    lines.append([*line])
     
# Get all possible crosses  
crosses = find_crosses(lines, "@")

most_power = 0   
for i in range(len(crosses)):
    for j in range(len(crosses)):
        
        if i == j:
            continue
        
        power = crosses[i].processors * crosses[j].processors
            
        if power > most_power and not collided(crosses[i], crosses[j]):
            most_power = power
       
print(most_power)