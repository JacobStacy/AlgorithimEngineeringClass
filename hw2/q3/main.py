from sys import stdin

stdin.readline()

labs = {}
max = -1
for line in stdin.readlines():
    lab_id = int(line)
    
    if lab_id not in labs:
        labs[lab_id] = 1
    else:
        labs[lab_id] += 1
    
    if max == -1:
        max = lab_id
        continue
    
    # More items than current max
    if labs[lab_id] > labs[max]:
        max = lab_id
    
    # Same number of items as current max
    if (labs[lab_id] == labs[max] and lab_id > max):
        max = lab_id
    
print(max)