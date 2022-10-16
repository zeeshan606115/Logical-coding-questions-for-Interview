# Find Largest Number After concating the element of List

# Approach 1
test_list = [1, 34, 3, 98, 9, 76, 45, 4]
n = []
nl = []
for i in test_list:
    n.append(str(i))
n1 = sorted(n, reverse = True)
s = ''.join(n1)
print(s)



# Approach 2 with permutation
from itertools import permutations
test_list = [23, 65, 98, 3, 4]

n = []
n = permutations(test_list)
nl = []

for i in list(n):
    s = ''
    for j in i:
        s += ''.join(str(j))
    nl.append(s)
    
print(int(max(nl)))
