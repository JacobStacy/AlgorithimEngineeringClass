from sys import stdin

testing = False

if not testing:
    line = stdin.readline().split(' ')
    n_hats, id = int(line[0]), int(line[1])

    colors = stdin.readline().split(' ')
    seen = stdin.readline().split(' ')
    
else:
    n_hats = 5
    colors = ["gainsboro",  "orange_peel", "fawn", "yellow", "white_smoke"]
    
    id = 0
    seen = ["orange_peel", "orange_peel", "gainsboro", "yellow"]
    id = 1
    seen = ["orange_peel", "orange_peel", "gainsboro", "yellow"]
    # id = 2
    # seen = ["orange_peel", "orange_peel", "gainsboro", "yellow"]
    # id = 3
    # seen = ["orange_peel", "orange_peel", "orange_peel", "yellow"]
    # id = 4
    # seen = ["orange_peel", "orange_peel", "orange_peel", "gainsboro"]

numbers = {}
for i in range(len(colors)):
    numbers[colors[i].strip()] = i


sum = 0
for color in seen:
    sum += numbers[color.strip()]
    
answer = -1
for i in range(n_hats):
    if (sum + i) % n_hats == id:
        answer = i % n_hats
        break
    
print(colors[answer].strip())
