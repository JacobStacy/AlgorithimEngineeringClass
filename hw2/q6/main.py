from sys import stdin

line = stdin.readline()

files = [0] # 0 place holder to move up index for indexing from 1
for file in stdin.readline().split(" "):
    files.append(int(file))
  
i = 1
out = ""
swap_i = -1
while i + 1 < len(files):
    
    if files[i] > files[i + 1]:
        if len(out) > 0:
            if swap_i != -1:
                out = f"swap {swap_i} {i + 1}"
                swap_i = -1
                i += 1
                continue
            else:
                print("no")
                exit()
            
        if i + 2 < len(files) and files[i + 1] > files[i + 2]:
            old_i = i
            while i + 1 < len(files) and files[i] > files[i + 1]:
                i += 1
                
            out = f"reverse {old_i} {i}"
            
        else:
            out = f"swap {i} {i + 1}"
            if len(files) > 3:
                swap_i = i
            
    i += 1
                
if swap_i == -1:
    print("yes")
    if len(out) > 0:
        print(out)
else:
    print("no")
            
        
        
        

    
