# sentence reversal
# "This is me" => "Me is This"

def rev_word1(s):
    return " ".join(reversed(s.split()))

def rev_word2(s):
    return " ".join(s.split()[::-1])

#interview setup

def rev_word3(s):
    words = []
    length = len(s)
    spaces = [" "]
    i = 0 
    
    while i < length:
        if s[i] not in spaces:
            word_start = 1
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start::i])
        i =+ 1
     
    return " ".join(reveresed(words))    

print(rev_word3("This is Pabi")) 