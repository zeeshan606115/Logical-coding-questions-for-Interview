def smallest_subarray(arr,s):
	start = 0
	min_size = float('inf')
	curr_sum = 0

	for end, val in enumerate(arr):
		curr_sum += val
		while curr_sum >= s:
			min_size = min(min_size, end - start + 1)
			curr_sum -= arr[start]
			start += 1
	return min_size

print(smallest_subarray([2,4,2,5,1],9))