# Recursive Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x): 
    if high >= low:
        mid = (high + low) // 2 # floor division
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        
        else: 
            return binary_search(arr, mid + 1, high, x)
      
    # element not present in the array  
    else: 
        return -1
    
arr = [ 2, 3, 4, 10, 40 ]
x = 10
low = 2
high = 4
print(binary_search(arr, low, high, x))
        