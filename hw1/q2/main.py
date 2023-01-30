import sys

for line in sys.stdin:
    
    line = line.split(' ')
    
    if len(line) < 2:
        continue
    
    score = int(line[0])
    
    for i in range(int(line[1])):
        if score % 2 == 0: # Even
            score -= 99
            score *= 3
        else: # Odd
            score -= 15
            score *= 2
        
        while score > 1000000 or score < 0:
            if score > 1000000:
                score -= 1000000
            elif score < 0:
                score += 1000000
            
    sys.stdout.write(str(score) + '\n')