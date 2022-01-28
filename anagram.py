# find the indicies of the 2 values which add up to a given number
# are all numbers positive or can there be negatives - no negatives
# are there any duplicates - no
# what to return if there is no solution - null
# will ther ealways be a solution - yes
# can there be multiple pairs that add up to the given number

# Anagram Check 
# given 2 strings see if they are anagrams , this is when letters of a string can be 
# rearranged to get a different meaningfull string

# sample - "public relations" -- "crap built on lies"

# if the strings are of equal length in characters
# is any input string empty

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    return sorted(s1) == sorted(s2) #not the optimal way

def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    #Edge Case
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
        
    return True
