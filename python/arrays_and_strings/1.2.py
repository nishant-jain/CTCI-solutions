# Write code to reverse a C-Style String (C-String means that "abcd" is represented as five characters, including the null character

def reverse_c_python(input_string):
	# just return reverse of the string given using list magic(the negative skip param with empty start ends)
	return input_string[::-1]

def reverse_c(input_string):
	# since strings are immutable in python, creating a new temporary list and then will convert to string.
	# Does python have a notion of null character at the end of strings??????
	temp_string = ''
	for i in input_string:
		return 
	#### todo

if __name__ == '__main__':
	assert reverse_c_python('reverse') == 'esrever'
	assert reverse_c_python('palindrome') == 'emordnilap'
	assert reverse_c_python('19991') == '19991'
	assert reverse_c('reverse') == 'esrever'
	assert reverse_c('palindrome') == 'emordnilap'
	assert reverse_c('19991') == '19991'