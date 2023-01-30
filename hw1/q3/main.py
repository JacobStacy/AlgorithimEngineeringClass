import sys

players = int(sys.stdin.readline())
    
line = sys.stdin.readline().split(' ')

poorest = 0
while (players >= 1):
    next_poorest = 999999
    
    for i in range(len(line)):
        if line[i] == "_":
            continue
        
        score = int(line[i]) - poorest
        
        if score <= 0:
            players -= 1
            line[i] = "_"
        else:
            line[i] = score
    
            if score < next_poorest:
                next_poorest = score
        
    poorest = next_poorest
    
    if players > 0:
        print(players)
    