from sys import stdin

testing = False


conn_map = dict()

n_sites, m_edges = [int(j) for j in stdin.readline().split(' ')]
lines = stdin.readlines()
    
for i in range(n_sites):
    conn_map[i] = set()

for i in range(m_edges):
    first, second = [int(j) for j in lines[i].split(' ')]
    conn_map[first].add(second)

def traverse(site, visited):
    
    for conn in conn_map[site]:
        if conn not in visited:
            visited.add(conn)
            traverse(conn, visited)
        

visited = set()
n_clusters = 0
for site in conn_map:
    if site not in visited:
        n_clusters += 1
        visited.add(site)
        traverse(site, visited)
    
        
print(n_clusters)
    




