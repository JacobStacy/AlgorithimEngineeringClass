from sys import stdin

testing = False


connection_map = dict()

if testing:
    n_sites, m_edges = [5, 7]
    lines = "0 1\n0 2\n0 3\n1 2\n1 3\n1 4\n2 3\n".split('\n')
else:
    
    n_sites, m_edges = [int(j) for j in stdin.readline().split(' ')]
    
    lines = stdin.readlines()
    
    
for i in range(n_sites):
    connection_map[i] = []

for i in range(m_edges):
    first, second = [int(j) for j in lines[i].split(' ')]
    connection_map[first].append(second)
    # connection_map[second].append(first)


def max_i(x):
    ind = 0
    max = -1
    
    for i in range(len(x)):
        if (val:=x[i]) >= max:
            ind = i
            max = val
            
    return ind


def find_most(conn_map, connected):
    max = 0
    for site, conns in conn_map.items():
        if site not in connected:
            total = 0
            for conn in conns:
                if conn not in connected:
                    total += conn
                    total += find_most(conn_map, {site}.union(connected).union(set(conns)))
            
            if total >= max:
                max = total
    return max
    

print(find_most(connection_map, set()) + 1)

    





