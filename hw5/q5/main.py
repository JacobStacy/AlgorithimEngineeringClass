from sys import stdin
import heapq

testing = True


# total = 0
conn_map = dict()
# n_conns = dict()
# edges = []

if testing:
    n_sites, m_edges = [5, 6]
    lines = "0 1 5\n0 2 10\n0 3 2\n1 3 3\n1 4 8\n3 4 1".split('\n')
    # n_sites, m_edges = [6, 10] #11
    # lines = "0 1 7\n0 3 0\n0 4 4\n1 2 3\n1 3 5\n1 4 5\n2 3 3\n2 4 7\n3 4 2\n3 5 3".split('\n')
    # n_sites, m_edges = [6, 15] #54
    # lines = "0 1 17\n0 2 13\n0 3 10\n0 4 11\n0 5 10\n1 2 11\n1 3 15\n1 4 15\n1 5 14\n2 3 12\n2 4 16\n2 5 12\n3 4 14\n3 5 10\n4 5 12".split('\n')
else:
    n_sites, m_edges = [int(j) for j in stdin.readline().split(' ')]
    lines = stdin.readlines()

for i in range(n_sites):
    conn_map[i] = set()

for i in range(m_edges):
    first, second, cost = [int(j) for j in lines[i].split(' ')]
    # edges.append((first,second,cost))
    
    conn_map[first].add((cost,second))
    conn_map[second].add((cost, first))
    
    # total += cost
    
    # if first in n_conns:
    #     n_conns[first] += 1
    # else:
    #     n_conns[first] = 1
    
    # if second in n_conns:
    #     n_conns[second] += 1
    # else:
    #     n_conns[second] = 1
        

visited = set()
min_edges = []
# def cheapest(site):
#     total = 0
#     visited.add(site)
    
#     # sites = sorted(conn_map[site], key=lambda x: x[1])
    
#     for cost, conn in conn_map[site]:
            
#         if conn not in visited:
#             heapq.heappush(min_edges, (cost,conn))
    
#     while len(min_edges) > 0:
#         new_site = heapq.heappop(min_edges)
#         if new_site[1] not in visited:
#             total += new_site[0]
#             total += cheapest(new_site[1])
            
                
            
            
            
#     return total


site = next(iter(conn_map)) # Grab the "first" site in the map

total = 0
while len(visited) < n_sites:
    visited.add(site)
    
    # sites = sorted(conn_map[site], key=lambda x: x[1])
    
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
                
            
            
        
        

        



        

    
        
# print(n_clusters)
    




