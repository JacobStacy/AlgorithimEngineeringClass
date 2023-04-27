from sys import stdin

n_verts, m_edges = [int(x) for x in stdin.readline().split(' ')]

vert_map = [set() for _ in range(n_verts)]

for i in range(m_edges):
    
    first, second = [int(x) for x in stdin.readline().split(' ')]
    
    vert_map[first].add(second)
    vert_map[second].add(first)
    
t_cycles = int(stdin.readline())

for i in range(t_cycles):
    tested = set()
    line = stdin.readline().split(' ')
    out = "YES"
    
    for j in range(len(line)):
        
        first = int(line[j])
        
        if j + 1 == len(line):
            second = int(line[0])
        else:
            second = int(line[j+1])
        
        if first in tested:
            out = "NO"
            break
        
        tested.add(first)
        
        if second not in vert_map[first]:
            out = "NO"
            break
            
    print(out)
