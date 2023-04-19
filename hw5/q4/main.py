from sys import stdin

testing = True


total = 0
conn_map = dict()
n_conns = dict()
edges = []

if testing:
    n_sites, m_edges = [5, 6]
    lines = "0 1 5\n0 2 10\n0 3 2\n1 3 3\n1 4 8\n3 4 1".split('\n')
    
    n_sites, m_edges = [6, 15] #54
    lines = "0 1 17\n0 2 13\n0 3 10\n0 4 11\n0 5 10\n1 2 11\n1 3 15\n1 4 15\n1 5 14\n2 3 12\n2 4 16\n2 5 12\n3 4 14\n3 5 10\n4 5 12".split('\n')
else:
    n_sites, m_edges = [int(j) for j in stdin.readline().split(' ')]
    lines = stdin.readlines()

for i in range(n_sites):
    conn_map[i] = set()

for i in range(m_edges):
    first, second, cost = [int(j) for j in lines[i].split(' ')]
    edges.append((first,second,cost))
    
    conn_map[first].add(second)
    conn_map[second].add(first)
    
    total += cost
    
    if first in n_conns:
        n_conns[first] += 1
    else:
        n_conns[first] = 1
    
    if second in n_conns:
        n_conns[second] += 1
    else:
        n_conns[second] = 1
        
edges.sort(key=lambda x: x[2])
total = 0
connected = set()
for edge in edges:
    if edge[0] not in connected or edge[1] not in connected:
        total += edge[2]
        connected.add(edge[0])
        connected.add(edge[1])
        
        
# Make a modified dijkstra's 
        
print(total)
        


    
    
    
    


def traverse(site, visited):
    
    for conn in conn_map[site]:
        if conn not in visited:
            visited.add(conn)
            traverse(conn, visited)

visited = set()


        

    
        
# print(n_clusters)
    




