# Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
#         arr = ['e','o','b', 'a','m','g', 'l']
# Output : go, me, goal. 



dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l', 'y']

for i in dict:
	s = ''
	for j in i:
	    if j not in arr:
		    break
	else:
	    print(i)
