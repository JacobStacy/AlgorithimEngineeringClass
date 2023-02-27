from sys import stdin
import statistics

line = stdin.readline()


nums = []

for line in stdin.readlines():
    line = line.split(" ")
    
    operation = line[0]
    x = int(line[1])
    
    if operation == 'r':
        try:
            nums.remove(x)
            while 1:
                try:
                    nums.remove(x)
                except:
                    print(statistics.median(nums))
                    break
        except:
            print("Wrong!")
    else:
        nums.append(x)
        # nums.sort()
        print(statistics.median(nums))
        