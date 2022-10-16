l = '(())()))()()()())()'


c = 0
mv = 0
st = []
for i in l:
	if i == '(':
		st.append('(')

	elif i == ')':
		if len(st) > 0:
			st.pop()
			c += 1
		else:
			mv = c
			c = 0

	if len(st) == 0:
		max_val = max(c, mv)

print(max_val)