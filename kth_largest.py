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
