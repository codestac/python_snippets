
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