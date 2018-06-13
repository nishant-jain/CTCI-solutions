# Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer NOTE: One or two additional variables are fine An extra copy of the array is not

def remove_duplicate_char(str_list):
	# O(n^2), go through each element, remove each element which is same as current
	# print('original', str_list) , pythonic solution, but not a great one
	for i in range(len(str_list)-1):
		for j in range(i+1, len(str_list)):
			if str_list[i] == str_list[j]:
				str_list[j] = ''
	# print(str_list)
	# print(('').join(str_list))
	return ('').join(str_list)

if __name__ == '__main__':
	assert remove_duplicate_char(list('nishant')) == 'nishat'