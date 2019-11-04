# We have to rotate the whole string one by one
# Example: Enter the String: zeeshan

# eeshanz

# eshanze

# shanzee

# hanzees

# anzeesh

# nzeesha

# zeeshan



def stringRotation(s):
	s1 = ''
	for i in range(len(s)):
		s1 = s[0]
		s = s[1:]
		s += s1
		print(s)
		print()

s = input("Enter the String: ")
print()
stringRotation(s)

