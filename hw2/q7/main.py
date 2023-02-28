from sys import stdin
import bisect

def get_median():
    if len(numbers) == 0:
        print('Wrong!')
        return
    elif len(numbers) % 2 == 0: # Even
        out = (numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) - 1]) / 2
    else: # Odd
        out = numbers[len(numbers) // 2]
        
    if int(out) == out:
        print(int(out))
    else:
        print(out)

line = stdin.readline()  

numbers = []
content = {}

for line in stdin.readlines():
    line = line.split(" ")
    
    operation = line[0]
    x = int(line[1])
    
    # Add
    if operation == 'a':
        bisect.insort(numbers, x) # This line is not from the below source
        if x in content:
            content[x] += 1
        else:
            content[x] = 1
        get_median()       
         
    # Remove
    elif x in content and content[x] > 0:
        del numbers[bisect.bisect_left(numbers, x)] # This line is from https://stackoverflow.com/a/17348367, it is used to delete the left most occurance of the value
        content[x] -= 1
        get_median()
    else:
        print("Wrong!")
        
