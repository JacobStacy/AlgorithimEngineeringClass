import random 
from copy import deepcopy
import time


def create_list(n):
    out = []
    random.seed(n)
    for i in range(n):
        out.append(random.randint(-100_000, 100_000))
    return out
    

def quick_sort(data, low, high):
    def split(data, low, high):
        # Choose a random pivot using median of 3
        mid = low + ((high-low) // 2)
        
        # Pick pivot
        pivot = data[high]
        
        # Check if each element is greater than the pivot
        greater = low - 1
        for j in range(low,high):
            if data[j] <= pivot:
                greater += 1
                
                # Swap greater element to the begining
                data[j] , data[greater] = data[greater], data[j]
         
        # Swap greater with high
        data[greater+1], data[high] = data[high], data[greater+1]
        
        return greater + 1
    
    if low < high:
        
        # Find pivot index
        pivot_i = split(data, low, high)
        
        # Left of pivot, smaller than pivot
        quick_sort(data, low, pivot_i - 1)
        
        # Right of pivot, larger than pivot
        quick_sort(data, pivot_i + 1, high)
        
    
    
    
avg_quick_times = []
for n in range(1_000):
    data = create_list(n)
    
    quick_times = []
    for _ in range(3):
        working_data = deepcopy(data)
        start_time = time.now()
        quick_sort(working_data, 0, len(working_data)-1)
        quick_times.append(time.now() - start_time)
    
    avg_quick_times.append(sum(quick_times) / 3)
        
print(avg_quick_times)
                