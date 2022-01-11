phonebook = {}
phonebook["john"] = 123456
phonebook["jack"] = 456789
phonebook["pabi"] = 789456

print(phonebook)

#alternatively it can be stored as

phonebook = {"john": 123456, "jack": 123456, "pabi": 123456}

print(phonebook)

#iterating over dictionaires

phonebook = {"john": 123456, "jack": 123456, "pabi": 123456}
for name in phonebook.items():
    print(name)
    
    
#remove a value
del phonebook["john"]
print(phonebook)

# alternativey we can use pop

phonebook.pop("pabi")
print(phonebook)


phonebook = {"john": 123456, "jack": 123456, "pabi": 123456}

phonebook["jake"] = 987456

phonebook.pop("jack")

if "jake" in phonebook:
    print("Jake is added in the dictionary")
if "jack" not in phonebook:
    print("Jack is removed from the list")
    
print(phonebook)

# find a name that appears twice in a list
# assume only one name is repeated
given_list = ['Tom', 'Pabi', 'Tom']
def appear_twice(given_list):
    dictn = {}
    for name in given_list:
        if name in dictn:
            return name
        else:
            dictn[name] = 1
    return ''

    
# sum of two numbers should be 10 
# do i need to print anything - yes the numbers and return nothing
# will there be integers - yes only integers
# will there be a 2 or mare pairs to show the addition to 10 - you can choose which one 
# numbers can be negative
# if there are no pairs taht add up to 10 - return nothing found

given_list = [1,3,4,6,5]

def sum_10(given_list):
    dictn = {};
    for num in given_num:
        if (10 - num) in dictn:
            print(str(10-num) + ',' + str(item))
            return
        else:
            dictn[num] = 1 #value can be anything but I kept 1.
    print('We dont have a pair that adds up to 10')        

