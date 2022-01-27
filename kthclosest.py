def kthclosest(arr, n, k):  #[1,2,3,4,5,6]   2 numbers closest to 4
    arr2 = []
    if k in arr:
    	for i in arr:
        	if arr[i] == k:
				arr2.append(arr[i-1])
        		arr2.append(arr[i+1])
		return arr2
	return "Not present"

print(kthclosest([1,2,3,4,5,6], 2, 4))