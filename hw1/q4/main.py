import sys

sys.stdin.readline()

for line in sys.stdin:
    
    line = line.split(" ")
    x, y, n = int(line[0]), int(line[1]), int(line[2]) - 1

    last_scores = [x,y]
    
    for i in range(n):
        scores = set()

        for score in last_scores:
            scores.add(score + x)
            scores.add(score + y)
        
        last_scores = scores
        
    print(*sorted(scores))     

    