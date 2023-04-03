from sys import stdin
import math

testing = True



if not testing:
    n_people, k_skills = [int(i) for i in stdin.readline().split(" ")]
    required_skills = set(stdin.readline().strip().split(" "))
    crewmates = []
    for i in range(n_people * 2):
        if i % 2 == 0:
            a = stdin.readline()
            continue
        
        skills = set()
        
        for skill in stdin.readline().strip().split(" "):
            if skill in required_skills:
                skills.add(skill)
                
        if len(skills) > 0:
            crewmates.append(skills)
        
else:
    n_people, k_skills = 15, 12
    required_skills = set("Botany Neuroscience ArtificialLife Batteries Metals InformationTheory".split(" "))
    crewmates = []
    # for line in "Botany Neuroscience ArtificialLife\nBotany Batteries\nBotany\nBotany Batteries Metals InformationTheory\nNeuroscience Batteries InformationTheory".split('\n'):
    #     skills = set()
        
    #     for skill in line.split(" "):
    #         if skill in required_skills:
    #             skills.add(skill)
                
    #     if len(skills) > 0:
    #         crewmates.append(skills)
    crewmates = [{'Medicine', 'Plastics', 'EvolutionaryBiology', 'Statistics'}, {'Cosmology', 'Plastics', 'Sensors', 'EvolutionaryBiology'}, {'Medicine', 'Cryptography', 'EvolutionaryBiology', 'Statistics'}, {'Medicine', 'Sensors', 'EvolutionaryBiology', 'Cosmology'}, {'AgentBasedModeling', 'Sensors', 'EvolutionaryBiology', 'AlienLanguages'}, {'Plastics', 'CloudComputing', 'Statistics', 'AgentBasedModeling'}, {'Medicine', 'Plastics', 'CloudComputing', 'Sensors'}, {'CloudComputing', 'Plastics', 'Polymers', 'AgentBasedModeling'}, {'Medicine', 'PersonalizedMedacine', 'Polymers', 'Statistics'}, {'Cosmology', 'Polymers', 'Statistics', 'AlienLanguages'}, {'PersonalizedMedacine', 'Cryptography', 'Statistics', 'AgentBasedModeling'}, {'Medicine', 'AgentBasedModeling', 'PersonalizedMedacine', 'AlienLanguages'}, {'PersonalizedMedacine', 'CloudComputing', 'Polymers', 'Cosmology'}, {'PersonalizedMedacine', 'Polymers', 'Cryptography', 'AlienLanguages'}, {'CloudComputing', 'Sensors', 'Cryptography', 'AlienLanguages'}]
    required_skills = {'PersonalizedMedacine', 'CloudComputing', 'AlienLanguages', 'Sensors', 'AgentBasedModeling', 'Cosmology', 'Plastics', 'Polymers', 'Medicine', 'Cryptography', 'EvolutionaryBiology', 'Statistics'}
    




# def least_needed(crewmates, skills, n_included):
    
#     if n_included > n_people:
#         return None
    
#     if len(skills) >= k_skills:
#         return n_included
    
#     include = least_needed(crewmates[:-1], skills.union(skills), n_included + 1)
#     dont = least_needed(crewmates[:-1], skills, n_included)
    
#     if include is None:
#         return dont
    
#     if dont is None:
#         return include
    
#     if include < dont:
#         return include
#     else:
#         return dont
    
# print(least_needed(crewmates, set(), 0))

def get_leading_bit(num):
    return 2**math.floor(math.log2(num))
    
def get_mate(num, crewmates):
    j = -1
    while 1:
        if num <= 0 or -j > len(crewmates):
            break
        
        if 1 & num:
            return crewmates[j]
        
        num>>=1
        j-=1
    
skills_under_num = {}

min = None
for i in range(1, 2**len(crewmates) - 1):
    j = -1
    skills = set()
    n_included = 1
    
    
    leading_bit = get_leading_bit(i)  
    if i == 32768:
        pass 
    crewmate = get_mate(leading_bit, crewmates)
    
    remaining = i ^ leading_bit
    
    if remaining:
        skills = crewmate.union(skills_under_num[remaining][0])
        n_included += skills_under_num[remaining][1]
    else:
        skills = crewmate
    

    skills_under_num[i] = (skills, n_included)
    
    if len(skills) >= k_skills:
        if min is None or n_included < min:
            min = n_included
            
    
        
print(min)