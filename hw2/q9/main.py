from sys import stdin
import heapq

class Job():
    in_time = 0
    duration = 0
    
    def __init__(self, in_time, duration):
        self.in_time = in_time
        self.duration = duration
    
    def __lt__(self, b):
        return self.duration < b.duration    


line = stdin.readline()

heap = []
first_job = None
for line in stdin.readlines() :
    line = line.split(" ")
    
    job = Job(int(line[0]), int(line[1]))
    heapq.heappush(heap, job)
    
    if first_job is None or job.in_time < first_job.in_time:
        first_job = job
    
job_total = len(heap)

current_time = first_job.in_time
sum_time = 0
for i in range(len(heap)):
    
    current_job = heapq.heappop(heap)
    
    job_holder = []
    first_job = None
    while current_time < current_job.in_time:
        job_holder.append(current_job)
        current_job = heapq.heappop(heap)
        
        if first_job is None or current_job.in_time < first_job.in_time:
            first_job = current_job
        
        if len(heap) == 0:
            current_time = first_job.in_time
            
            for job in job_holder:
                heapq.heappush(heap, job)
            
    for job in job_holder:
        heapq.heappush(heap, job)
    
    current_time += current_job.duration
    sum_time += current_time - current_job.in_time

print(sum_time // job_total)