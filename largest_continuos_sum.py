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
        