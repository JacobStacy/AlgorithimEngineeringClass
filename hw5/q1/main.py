from sys import stdin

connection_map = dict()
 
n_sites, m_edges = [int(j) for j in stdin.readline().split(' ')]
lines = stdin.readlines()
    
for i in range(n_sites):
    connection_map[i] = set()

for i in range(m_edges):
    first, second = [int(j) for j in lines[i].split(' ')]
    connection_map[first].add(second)
    connection_map[second].add(first)

max = 0
for site, conns in connection_map.items():
    total = 0
    for i in range(len(conns)):
        total += len(conns) - i
        
    if total > max:
        max = total
        
print(max)
    




