from sys import stdin
import math

testing = False

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
    
    


min = None
for i in range(2**len(crewmates)):
    skills = set()
    ii = i + 1
    j = -1
    n_included = 0
    
    while 1:
        if ii <= 0 or -j > len(crewmates):
            break
        
        if 1 & ii:
            skills = skills.union(crewmates[j])
            n_included += 1
            
            
            if n_included > n_people or n_included >= min:
                break
                
            if len(skills) >= k_skills:
                if min is None or n_included < min:
                    min = n_included
                    
        j -= 1       
        ii>>=1
        
print(min)