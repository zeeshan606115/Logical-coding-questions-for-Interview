# Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
#         arr = ['e','o','b', 'a','m','g', 'l']
# Output : go, me, goal. 



dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l', 'y']

for i in dict:
	s = ''
	c = 0
	for j in range(len(i)):		
		if (i[c] in arr):
			s = s + i[c]
			c +=1
	if (s in dict):
		print(s)