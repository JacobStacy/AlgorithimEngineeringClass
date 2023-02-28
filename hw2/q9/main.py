from sys import stdin
import heapq

class Job():
    in_time = 0
    duration = 0
    
    def __init__(self, in_time, duration):
        self.in_time = in_time
        self.duration = duration
        
    def __gt__(self, b):
        return self.duration > b.duration
            
    def __lt__(self, b):
        return self.duration < b.duration    
    
    def __eq__(self, b):
        return self.duration == b.duration


stdin.readline()

heap = []
for line in stdin.readlines():
    line = line.split(" ")
    heapq.heappush(heap, Job(int(line[0]), int(line[1])))
    
sum_time = 0
job_total = len(heap)
for i in range(len(heap)):
    job = heapq.heappop(heap)
    sum_time += (sum_time - job.in_time) + job.duration

print(sum_time // job_total)