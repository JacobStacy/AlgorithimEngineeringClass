from sys import stdin

rarity = dict()
have_skill = dict()
ids = dict()

previous = dict()

n_people, k_skills = [int(i) for i in stdin.readline().split(" ")]
all_skills = stdin.readline().strip().split(" ")
required_skills = set(all_skills)
crewmates = set()

for i in range(n_people * 2):
    if i % 2 == 0:
        stdin.readline()
        continue
    
    skills = set()
    line = stdin.readline().strip()
    if line in previous:
        continue
    previous[line] = None
    for skill in line.split(" "):
        
        if skill in required_skills:
            if skill not in rarity:
                rarity[skill] = 1
            else:
                rarity[skill] += 1
            skills.add(skill)
            if skill not in have_skill:
                have_skill[skill] = [len(crewmates)]
            else:
                have_skill[skill].append(len(crewmates))
                
        
    if len(skills) > 0:
        ids[len(crewmates)] = skills
        crewmates.add(len(crewmates))
            




def find_min(skills_required, current_min, selected):
    
    min = current_min
    
    for crewmate in have_skill[sorted(skills_required, key=lambda x: rarity[x])[0]]:
        
        if crewmate in selected:
            continue
        
        c_skills = set()
        
        for c_skill in ids[crewmate]:
            c_skills.add(c_skill)
        
        skills_left = skills_required-c_skills
        
        under = 0
        if len(skills_left) != 0:
            under = find_min(skills_left, min, selected.union({crewmate}))
        
            if under is None:
                continue
        
        if min > 1 + under:
            min = 1 + under
            
    return min
    

print(find_min(required_skills,n_people,set()))