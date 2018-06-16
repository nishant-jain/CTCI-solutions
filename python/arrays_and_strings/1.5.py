# Write a method to replace all spaces in a string with %20

def replace_space_python(input_str):
	# split and then join with replacement string
	return ("%20").join(input_str.split(' '))

def replace_space(input_str):
	# count spaces, generate new array of apt size(not required in python), then create new string
	space_ct = 0
	for i in input_str:
		if i == ' ':
			space_ct += 1
	# print space_ct
	output_list = list()

	for i in input_str:
		if i != ' ':
			output_list.append(i)
		else:
			output_list.append('%')
			output_list.append('2')
			output_list.append('0')
		# print output_list
	return ('').join(output_list)

if __name__ == "__main__":
	assert replace_space_python(" hello world ") == "%20hello%20world%20"
	assert replace_space(" hello world ") == "%20hello%20world%20"