""" 
sets - unordered collection of unique items
"""
tags = {"python","ai","ml"}
print(tags)
print("ai" in tags)
tags.add("rag")
tags.add("ai")
print(tags)
tags.discard("ml")
print(tags)

 # empty = {} - declares an empty dict not set
#  empty = set()
 #use sets to dedup any list
sigups = ["a@x.com","b@.com","a@x.com","c@x.com"]
unique_signups = set(sigups)
print(unique_signups)
 
#set algebra
arjit_skills = {"python","ai","devops","containers"}
rohit_skills = {"python","git","devops","aws"}
print("both know", arjit_skills & rohit_skills)
print("either knows |", arjit_skills | rohit_skills)
print("only arjit ",  arjit_skills - rohit_skills)
print("exactly one ",arjit_skills ^ rohit_skills)