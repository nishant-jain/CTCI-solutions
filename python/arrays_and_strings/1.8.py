# Assume you have a method isSubstring which checks if one word is a substring of another Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i e , "waterbottle" is a rotation of "erbottlewat")

def is_rotation(str1, str2):
	if((len(str1) == len(str2)) and (str1 in str2+str2)):
		return True
	else:
		return False

if __name__ == "__main__":
	assert is_rotation("waterbottle", "erbottlewat") == True
	assert is_rotation("waterbottl", "erbottlewat") == False
	assert is_rotation("apple", "apple") == True