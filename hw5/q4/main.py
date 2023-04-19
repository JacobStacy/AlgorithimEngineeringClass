from sys import stdin
import heapq

n_sites = int(stdin.readline().split(' ')[0])

conn_map = dict()
for i in range(n_sites):
    conn_map[i] = set()

for line in stdin.readlines():
    first, second, cost = [int(j) for j in line.split(' ')]
    
    conn_map[first].add((cost, second))
    conn_map[second].add((cost, first))


visited = set()
min_edges = []

site = next(iter(conn_map)) # Grab the a site in the map
total = 0
while len(visited) < n_sites:
    visited.add(site)
    
    for cost, conn in conn_map[site]:
        if conn not in visited:
            heapq.heappush(min_edges, (cost,conn))
    
    while len(min_edges) > 0:
        new_site = heapq.heappop(min_edges)
        if new_site[1] not in visited:
            total += new_site[0]
            site = new_site[1]
            break
            
print(total)