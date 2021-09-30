lst = [3,4,20,6,15,2,1,7]
max_num = lst[-1]

length = len(lst)
for i in range(length-2, -1, -1):
	if max_num > lst[i]:
		lst[i] = max_num
	else:
		max_num = lst[i]

print(lst)