from sys import stdin

stdin.readline()  

hives = []
warriors = 0
start = 0
for line in stdin.readlines():
     
    line = line.split(" ")
    hives.append((int(line[0]), int(line[1])))
    
    while warriors < 0:
        warriors -= hives[start][0] - hives[start][1]
        start += 1
        
    warriors += hives[-1][0] - hives[-1][1]

print(start)
        
        
