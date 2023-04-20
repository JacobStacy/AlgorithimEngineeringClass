
from sys import stdin

testing = False

edges_made = set()
conn_map = dict()
edges = []
if testing:
    n_sites, m_edges = [5, 6]
    lines = "0 1\n0 2\n0 4\n1 4\n2 3\n2 4\n".split('\n')
    n_sites, m_edges = [7, 7]
    lines = "0 1\n0 2\n0 4\n1 4\n2 3\n2 4\n99 100\n".split('\n')
    n_sites, m_edges = [4, 4]
    lines = "0 1\n1 2\n2 3\n3 0".split('\n')
    
    n_sites, m_edges = [15, 40] #9
    lines = ['0 1', '0 9', '1 4', '1 5', '1 10', '1 11', '1 12', '1 13', '2 5', '2 7', '2 8', '2 10', '2 12', '2 13', '3 6', '3 7', '3 11', '4 5', '4 8', '5 7', '5 8', '5 11', '5 14', '6 7', '6 8', '6 12', '7 9', '7 11', '7 14', '8 9', '8 10', '8 11', '8 12', '8 14', '9 14', '10 11', '10 12', '11 13', '12 13', '12 14']
else:
    n_sites, m_edges = [int(j) for j in stdin.readline().split(' ')]
    lines = stdin.readlines()


for i in range(m_edges):
    first, second = [int(j) for j in lines[i].split(' ')]
    edges.append((first, second))
    # edges.append((second, first))
    # edges_made.add((first,second))
    # edges_made.add((second,first))
    
    if first not in conn_map:
        conn_map[first] = set()
    if second not in conn_map:
        conn_map[second] = set()
    conn_map[first].add(second)
    conn_map[second].add(first)
    
# def rarity(x):
#     first = len(conn_map[x[0]])
#     second = len(conn_map[x[1]])
#     if first < second:
#         return first
#     return second

cache = dict()

def find_min(unsecured, curr_min, secured, dont_include):
    
    
    if len(secured) + 1 > len(curr_min):
        return None
    
    if f"{unsecured}{dont_include}" in cache:
        return cache[f"{unsecured}{dont_include}"]
    
    min = curr_min
    
    n_checked = 0
    i = 0
    while 1:
        for edge in sorted(unsecured, key=lambda x: len(conn_map[x[0]])):
        # for edge in sorted(unsecured, key=lambda x: len(conn_map[x[0]]), reverse=True):
        # for edge in unsecured:
            for conn in conn_map[edge[0]]:
                
                
                if conn in secured or conn in dont_include:
                    continue
                
                n_checked += 1
                
                sites_left = set()
                for site in unsecured:
                    if site[0] == conn or site[1] == conn:
                        continue
                    sites_left.add(site)
                
                
                
                if len(sites_left) != 0:
                    under = find_min(sites_left, min, {conn}.union(secured), dont_include)
                    result = find_min(unsecured, min, secured, dont_include.union({conn}))
                else:
                    under = secured.union({conn})
                    result = under 
                
                
                if under is None and result is not None:
                    under = result
                
                if under is not None and result is not None:
                    if len(result) < len(under):
                        under = result
                        
                if under is None and result is None:
                    break
                
                        
                if min is None or len(min) > len(under):
                    min = under
                
            if n_checked > 0:
                break
            
        if n_checked == 0 and i != 1:
            i = 1
            continue
        
        break
            

    if n_checked == 0:
        out = None
    else: 
        out = min
        
    cache[f"{unsecured}{dont_include}"] = out
    
    return out

result = find_min(edges, set((range(n_sites))), set(), set())
print(len(result))
if testing:
    print(result)
    



