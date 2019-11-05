# Write a function that returns a character mapping from a word.

# Examples:-
# character_mapping("abcd") ➞ [0, 1, 2, 3]

# character_mapping("abb") ➞ [0, 1, 1]

# character_mapping("babbcb") ➞ [0, 1, 0, 0, 2, 0]

# character_mapping("hmmmmm") ➞ [0, 1, 1, 1, 1, 1]



def stringMapping(s):
	dict = {}
	j = 0
	l = []

	for i in s:
		if i not in dict:
			dict[i] = j
			l.append(dict[i])
			j += 1

		else:
			dict[i] = dict.get(i)
			l.append(dict[i])

	return l


s = input("Enter Any String: ")
z = stringMapping(s)
print(z)


