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