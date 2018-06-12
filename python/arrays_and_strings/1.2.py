# Write code to reverse a C-Style String (C-String means that "abcd" is represented as five characters, including the null character

def reverse_c_python(input_string):
	# just return reverse of the string given using list magic(the negative skip param with empty start ends)
	return input_string[::-1]

def reverse_c(input_string):
	# since strings are immutable in python, creating a new temporary list and then will convert to string.
	# Python doesn't have a null character at the end of strings, as far as normal developers are concerned
	# added a null (\0) manually to simulate C strings
	temp_string = list()
	for i in input_string[:-1]:
		temp_string.insert(0, i)
	temp_string.append('\0')
	return ('').join(temp_string)

if __name__ == '__main__':
	assert reverse_c_python('reverse') == 'esrever'
	assert reverse_c_python('palindrome') == 'emordnilap'
	assert reverse_c_python('19991') == '19991'
	assert reverse_c('reverse\0') == 'esrever\0'
	assert reverse_c('palindrome\0') == 'emordnilap\0'
	assert reverse_c('19991\0') == '19991\0'