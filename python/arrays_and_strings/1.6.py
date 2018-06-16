# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_image(arr):
	# O(nm) for both swaps
	# first swap on the middle column, then swap on the minor diagonal(45 deg)
	# middle column swap
	rlen = len(arr)
	clen = len(arr[0])
	for i in range(len(arr)):
		for j in range(len(arr[0])/2):
			arr[i][j], arr[i][clen-1-j] = arr[i][clen-1-j], arr[i][j]
	# diagonal swap
	for i in range(len(arr)):
		for j in range(len(arr[0]) - i):
			arr[i][j], arr[rlen-j-1][clen-i-1] = arr[rlen-j-1][clen-i-1], arr[i][j]

	return arr

if __name__ == '__main__':
	assert rotate_image([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
	assert rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2] , [9, 6, 3]]