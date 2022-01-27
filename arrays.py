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


####################################
# array pair sum
# output all the unique pairs that have the sum of a specific value

# [1,2,3,4] 6

def find_sum(arr, k):
    
    #Edge case
    if len(arr) < 2:
        return "Less than 2 array list"
    
    #Sets for tracking
    seen = set()
    output = set()
    
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))
    #return len(output)
    print('\n'.join(map(str,list(output))))
    
print(find_sum([1,3,2,3,4], 6))


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
        
# largest continous sum 
# it can have all negative numbers
# [1,3,-3] => 4

def large_cont_sum(arr):
    if len(arr):
        return 0
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]: #skip the first element
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
        
    return max_sum
        
        
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


################################
# first and last index of a target in an array
# [2,3,4,5,5,5,5,6,7] , target 5 = > [3, 6] if not found return [-1, -1]
# time complexity O(n) space complexity O(n)

def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
                return [start, i]
            
    return [-1, -1]

# with a binary search if the array is already sorted

def find_start(arr, target):
    if arr[0] == target:
        return 0
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    
    left, right = 0, len(arr) -1
    
    while left <= right:
        mid == (left + right) // 2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def first_and_last(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
            return [-1, -1]
        
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]
    
# As we are using BInary search Time complexity is 2 * O(log n) => O(log n)


## kth largest element in an array
## arr = [4,2,9,7,5,6,7,1,3]
## k = 4, output: 6 = > 1st largest element is 9, 2nd largetst is 7, 3rd large is 7, 4th large is 6

def kth_largest(arr, k):
    for i in range(k - 1):
        arr.remove(max(arr))
    return max(arr)

# this has a time complexity of 2(k-1(n)= 2kn - n = O(kn)
# space complexity is O(n)

# this can be completed by sorting

def kth_large_sort(arr, k):
    n = len(arr)
    arr.sort() #O(nlogn)
    return arr[n - k] #O(1)


# 2 numbers in array that add up to 11

def sum(arr, k):
    for i in arr:
        target = arr[i] - k
        if target in arr:
            return (min(target, arr[i]), max(target, arr[i]))
        else:
            return False

 
            