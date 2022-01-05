def second_largest(arr):
    largest = None
    second_largest = None
    if (arr.length == 0 or arr.length == 1):
        return False
    else:
		for current_num in arr:
			if largest == None:
				largest = current_num
			elif current_num > largest:
				second_largest = largest
				largest = current_num
			elif second_largest == 0:
				second_largest = current_num
 			elif second_largest > current_num:
				second_largest = current_num
    
    return second_largest
        
			