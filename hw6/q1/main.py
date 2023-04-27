from sys import stdin

n_verts, m_edges, k_testing = [int(x) for x in stdin.readline().split(' ')]
    
vert_map = [set() for x in range(n_verts)]

for line in stdin.readlines():
    
    first, second = [int(x) for x in line.split(' ')]
            
    vert_map[first].add(second)
    vert_map[second].add(first)
    
edges_pos = (n_verts * (n_verts - 1)) // 2
print(n_verts, edges_pos - m_edges, n_verts - k_testing)

out = []

for vert_i in range(n_verts):
    vert = vert_map[vert_i]
    
    for i in range(n_verts):
        if i == vert_i:
            continue
        
        if i not in vert and vert not in vert_map[i]:
            vert_map[vert_i].add(i)
            vert_map[i].add(vert_i)
            print(vert_i, i)
            
    