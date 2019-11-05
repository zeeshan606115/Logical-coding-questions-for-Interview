# In this program we will first find the shared letters in both string
# Then we will find unique letter in first strinjg and then unique letter in second String




def StringManipulation(s1, s2):
	shared = ''
	s1Unique = ''
	s2Unique = ''
	s1 = s1.casefold()
	s2 = s2.casefold()
	for i in  s1:
		if i in s2:
			shared += i

		elif i not in s2:
			s1Unique += i

	for j in s2:
		if j not in s1:
			s2Unique += j

	print("Shared letters: ",shared)
	print("Unique letters in first String: ",s1Unique)
	print("Unique letters in second String: ",s2Unique)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
StringManipulation(s1, s2)
