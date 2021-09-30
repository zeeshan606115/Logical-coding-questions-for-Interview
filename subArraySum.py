def subArraysum(nums, target):
	curr_sum = 0
	start = 0
	for i in range(len(nums)):
		
		if curr_sum == target:
			print("Found")
			print(start, i)
			return 1
		curr_sum += nums[i]
		while (curr_sum > target):
			curr_sum -= nums[start]
			start += 1
	print('not Found')
	return 0
print(subArraysum([1,2,3,4,44], 44))
