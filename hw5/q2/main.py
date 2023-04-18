from sys import stdin

conn_map = dict()
edges = []

n_sites, m_edges = [int(j) for j in stdin.readline().split(' ')]
lines = stdin.readlines()
    
for i in range(n_sites):
    conn_map[i] = set()

for i in range(m_edges):
    first, second = [int(j) for j in lines[i].split(' ')]
    conn_map[first].add(second)
    conn_map[second].add(first)
    edges.append((first,second))

max = 0
for edge in edges:
    first = conn_map[edge[0]]
    second = conn_map[edge[1]]
    
    if (n:=len(first.union(second))) > max:
        max = n
        
print(max * (max-1) // 2)
    




