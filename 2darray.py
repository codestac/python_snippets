a_2d = [[1,2,3],[4,5,6]]
print(a_2d)

a_2d[1][1] = 99
print(a_2d)

for row in a_2d:
    for item in row:
        print(item)
        
for row in range(len(a_2d)):
	for item in range(len(a_2d[row])):
		print(a_2d[row][item])
  
# diagonal sum of a 2d array/list hint: diagonals have same index
# its always 2 dimensional
def diagonal_sum(given_2d):
	total = 0
	for i in range(len(given_2d)):
		total += given_2d[i][i]
	return total
    
print(diagonal_sum(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]))


# question : check if the the rooks are safe challenge
# clarifying questions: 
# whats the size of the chess board? 2X2 or 99X99
# is it always sqaure shaped? col = rows
# could the size of the array be empty? atleast 1X1

def rooks_are_safe(arr):
    n = len(arr)
    for i in range(n): #row selection first
        row_count = 0
        for j in range(n):
            row_count += arr[i][j]
        if row_count > 1:
            return False
    
    for j in range(n): #col selection second
        col_count = 0
        for i in range(n):
            col_count += arr[i][j]
            print(arr[i][j])
        if col_count > 1:
            return False
    return True

print(rooks_are_safe(
	[[1,0,0],
     [0,1,0],
     [0,0,1]]
))