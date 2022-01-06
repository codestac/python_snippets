# find the number of negative numbers in the 2d array 
# find the time complexity

# clarifying questions
# is the array always square shaped - yes
# what about 0 - not counted as negative number
def find_negative(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i][j] < 0):
                count +=1
        return count
    
print(find_negative([[-1,0],[-2, -1]]))

#optimal solution
def count_negative(arr):
    count = 0
    row_i = 0
    col_i = len(arr[0]) - 1
    while col_i >= 0 and row_i < len(arr):
        if arr[row_i][col_i] < 0:
            count += (col_i + 1)
            row += 1
        else:
            col_i -=1
    return count