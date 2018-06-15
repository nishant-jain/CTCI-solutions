# Write a method to decide if two strings are anagrams or not.

def is_anagram(str1, str2):
	# sorting and comparing would return is strings are anagrams. O(n), assuming comparison takes n checks
	if(sorted(str1)==sorted(str2)):
		return True
	else:
		return False

def is_anagram_unsort(str1, str2):
	# create dictionary with count of each character, should be equal in second string , O(n)
	
	counter = dict()
	# uniq_char = 0
	# processed_char = 0
	for i in str1:
		if counter.get(i):
			counter[i] += 1
		else:
			counter[i] = 1
			# uniq_char += uniq_char
	for i in str2: 
			if counter.get(i):
				counter[i] -= 1
				# if counter.get(i) == 0:
				# 	processed_char += processed_char
				# 	if uniq_char == processed_char:
				# 		return 
			else:
				return False
	for keys in counter.keys():
		if counter.get(keys,0) > 0:
			return False
	return True  

if __name__ == "__main__":
	assert is_anagram("hello", "lloeh") == True
	assert is_anagram("hello", "loeh") == False
	assert is_anagram("abcdef", "abcdefg") == False
	assert is_anagram("abcdef", "abcdeg") == False
	assert is_anagram_unsort("hello", "lloeh") == True
	assert is_anagram_unsort("hello", "loeh") == False
	assert is_anagram_unsort("abcdef", "abcdefg") == False
	assert is_anagram_unsort("abcdef", "abcdeg") == False