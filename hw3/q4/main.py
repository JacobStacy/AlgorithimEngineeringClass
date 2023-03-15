from sys import stdin

n_tests = int(stdin.readline())
    
# Finds best hours under each chunk
def find_max_under(chunk, frequencies, max_under):
    
    max = 0
    # Loop through every frequency and find the max
    for i in range(len(frequencies)):
        
        # Skip if not a valid frequency
        if chunk % frequencies[i] != 0 or chunk <= frequencies[i]:
            continue
        
        # Check if chunks made by new frequency can be broken up further and cache it
        if frequencies[i] not in max_under and i + 1 <= len(frequencies):
            max_under[frequencies[i]] = find_max_under(frequencies[i], frequencies[i+1:], max_under)  
        
        # Check if the the frequency is better than the last
        chunks_created = 1 + ((chunk // frequencies[i]) * max_under[frequencies[i]])
        if chunks_created >= max: max = chunks_created
               
    return max

for i in range(n_tests):
    
    crystal = int(stdin.readline().split(" ")[0])
    frequencies = sorted([int(i) for i in stdin.readline().split(" ")], reverse=True)
    
    print(find_max_under(crystal, frequencies, {}))

                
    
                    
                    
    