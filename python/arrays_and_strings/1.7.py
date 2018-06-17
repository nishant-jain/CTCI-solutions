# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0

def row_col_0(arr):
	# O(mn) solution with extra mem. Iterate over the original and maintain arrays for columns and rows which have 0s. 
	# Iterate again, and mark 0 wherever row in rlist or column in clist.
	clist = []
	rlist = []
	# print "input"
	# print arr
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if(arr[i][j] == 0):
				rlist.append(i)
				clist.append(j)
	# print rlist, clist
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if(i in rlist or j in clist):
				arr[i][j] = 0;
	# print "output"
	# print arr
	return arr

if __name__ == '__main__':
	assert row_col_0([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
	assert row_col_0([[0, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 11, 12], [0, 0, 15, 16]]
	assert row_col_0([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) == [[1, 2, 0], [4, 5, 0], [0, 0, 0]]