##############################################
# find the missing value from the second array
# [1,2,3,4,5] & [1,2,3,4]

# it doesnt have negative values
# it can have duplicates
# it is not empty
# value removed is present in atleast one array

def finder(arr1, arr2):
    arr1.sort()
    arr1.sort()
    
    #zip creates tuples which turns [1,2,3], [4,5,6] => (1,4), (2,5), (3,6)
    for num1, num2 in zip(arr1, arr2): #not an optimal solution
        if num1 != num2:
            return num1
    return arr1[-1]

# a more linear approach
import collections
def finder2(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
            
# a more sophisticated approach
def finder3(arr1, arr2):
    result = 0
    
    #perform XOR between the numbers in the array
    for num in arr1 + arr2:
        result ^= num
        print(result)
    
    return result