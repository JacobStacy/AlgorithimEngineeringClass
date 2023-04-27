from sys import stdin
import time
start_time = time.time()
n_avail, k_needed = [int(x) for x in stdin.readline().split(' ')]

rarity = dict()
have_skill = dict()
crew = []
for i in range(n_avail):
    stdin.readline()
    crew.append(set())
    
    for skill in stdin.readline().split():
        skill = int(skill)
        
        if skill not in have_skill:
            have_skill[skill] = []
            
        if skill not in rarity:
            rarity[skill] = 0
            
        have_skill[skill].append(i)
        rarity[skill] += 1
        crew[i].add(skill)

def check_time(time_stuff):
    if time.time() - time_stuff[0] >= 9.75:
        print(len(time_stuff[1]))
        print(*sorted(time_stuff[1]))   
        exit()

skills = set()

def find_skills(needed, selected, time_stuff):
    
    with_skill = have_skill[sorted(needed, key=lambda x : rarity[x])[0]]
    with_skill.sort(key=lambda x: len(crew[x]))
    
    best = None
    best_i = 0
    for i in with_skill:
        
        if i in selected:
            continue
        
        check_time(time_stuff)
        remaining = needed - crew[i]
        if best is None or len(remaining) < len(best):
            best = remaining
            best_i = i
    
    selected.add(best_i)        
    out = [best_i]
    
    check_time(time_stuff)
    if len(best) > 0:
        for skill in find_skills(best, selected, time_stuff):
            out.append(skill)
    
    return out


best = None
for i in range(len(crew)):
    result = [i]
    for i in find_skills(set(range(k_needed)) - crew[i], set(), (start_time, best)):
        result.append(i)
    if best is None or len(result) < len(best):
            best = result
            
    check_time((start_time, best))

print(len(best))
print(*sorted(best))