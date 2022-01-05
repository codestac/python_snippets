# print each character in a string
a_string = "abc"

for char in a_string:
    print(char)
    
for char in range(len(a_string)):
    print(a_string[char])
    
# string is reverse of itself check
def reverse_string(string1, string2):
    for char1 in range(len(string1)):
        char2 = len(string2) - char1 - 1
        if string1[char1] != string2[char2]:
            return False
        else:
            continue
    return True

print(reverse_string("ABC", "CBA"))

# string comparision if the first number is greater than the second
# check if the string length
def string_compare(str1, str2):
    if (len(str1) > len(str2)):
        return True
    elif (len(str1) < len(str2)):
        return False
    
    for i in range(len(str1)):
        if(str1[i] == str2[i]):
            continue
        elif(str1[i] > str2[i]):
            return True
    return False
    
print(string_compare("ABC", "CBA"))