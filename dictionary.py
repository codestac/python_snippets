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

    


