import sys

# Max-Heap would probably be best but this works and I am in a hurry
capacity = int(sys.stdin.readline().split(" ")[1])

infestations = []
for line in sys.stdin.readlines():
    infestations.append(int(line))

infestations.sort(reverse=True)
for i in range(len(infestations)):
    if i >= capacity:
        break
    print(infestations[i])
    
    