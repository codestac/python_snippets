#anagrams using Hash table

def anagram(s1, s2):
    if len(s1) != len(s2):
        return "Not an anagram"
    
    freq1 = {}
    freq2 = {}
    
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
        
    for ch in s2:
        if ch in frq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
            
    for key in freq1:
        if key not in freq2 and freq1[key] != freq2[key]:
            return False
    return True