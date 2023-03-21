from sys import stdin

line = stdin.readline()
n_hats, id = int(line[0]), int(line[1])
    
    
 

colors = stdin.readline().split()
seen = stdin.readline().split()

numbers = {}
for i in range(colors):
    numbers[colors] = i


sum = 0
for color in seen:
    sum += numbers[color]
    
print(sum % n_hats)