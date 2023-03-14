from sys import stdin
import heapq

testing = True

if not testing:
    n_tests = int(stdin.readline())
else:
    n_tests = 1


for i in range(n_tests):
    if not testing:
        crystals = [int(stdin.readline().split(" ")[0])]
        frequencies = sorted([int(i) for i in stdin.readline().split(" ")], reverse=True)
    else:
        crystals = [int("12 3".split(" ")[0])]
        frequencies = sorted([int(i) for i in "2 3 4".split(" ")], reverse=True)
        
        crystals = [int("84 4".split(" ")[0])]
        frequencies = sorted([int(i) for i in "42 7 6 3".split(" ")], reverse=True)
        
        crystals = [int("64 5".split(" ")[0])]
        frequencies = sorted([int(i) for i in "2 4 8 16 64".split(" ")], reverse=True)
    hours = 0
    
    max_under = {}
    
    
def find_max_under(freq, frequencies, max_under):
    
    
    max = 0
    for i in range(len(frequencies)):
        frequencies[i]
    