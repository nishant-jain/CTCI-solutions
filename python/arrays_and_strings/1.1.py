# Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures
# base solution without any extra mem is to iterate over all characters, and match with every other character, O(n^2)

def uniq_string_no_mem(test_string):
	'''
	sort the string first  O(lg n), then check every consecutive element for equality
	may take up extra space for sorting
	'''
	temp = sorted(test_string);

	for i in range(len(temp)-1):
		if(temp[i] == temp[i+1]):
			return "non-unique"
	return "unique"

def uniq_string_extra_mem(test_string):
	'''
	iterate over string, maintain a dictionary/list(as it also allows ) of encountered characters, return non-unique if character already exists
	O(n), although takes O(n) extra space too.
	'''
	char_counter = dict()
	for i in test_string:
		if i in char_counter:
			return "non-unique"
		else:
			char_counter[i] = 1
	return "unique"

if __name__ == '__main__':
	# used assert, yeah!
	assert uniq_string_no_mem("aquickbrown") == "unique"
	assert uniq_string_no_mem("nonunique") == "non-unique"
	assert uniq_string_extra_mem("aquickbrown") == "unique"
	assert uniq_string_extra_mem("nonunique") == "non-unique"
