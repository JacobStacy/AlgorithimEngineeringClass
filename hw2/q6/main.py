from sys import stdin

line = stdin.readline().split(" ")
change = ""

files = [1]
for file in stdin.readline().split(" "):
    files.append(int(file))
    
out_of_order = False
i = 1
out = ""
while i < len(files):
    
    if files[i - 1] > files[i]:
        if len(out) > 0:
            print("no")
            exit()
        
        old_i = i
        while files[i - 1] > files[i]:
            i += 1
            
        if i > old_i:
            out = "reverse"
        else:
            out = "swap"     
    
    i += 1
    
print("no")
print(out)