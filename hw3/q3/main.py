from sys import stdin
import queue

line = stdin.readline().split(" ")
length = int(line[0])
shift = int(line[1])

bits = [int(i) for i in [*stdin.readline()][:-1]]

message = [bits[0]]
last_few = queue.Queue(shift)
last_few.put(bits[0])
current = bits[0]
for i in range(1, length):
    
    next = current ^ bits[i]
    last_few.put(next)
    message.append(next)
    
    current = current ^ next
    
    if last_few.full():
        current = current ^ last_few.get()
        
print(*(message[:length]), sep="")
