def get_three_sum(arr, target):
	l1 = 0
	left = 1
	right = len(arr)-1
	while l1 < len(arr):
		while left < right:
			if arr[left] + arr[right] == target - arr[l1]:
				return ([arr[l1], arr[left], arr[right]])
			if arr[left] + arr[right] > target - arr[l1]:
				right -= 1
			else:
				left += 1
		l1 += 1
		left = l1 +1
		right = len(arr) - 1

	return ([-1, -1, -1])

print(get_three_sum([1,2,5,7,12], 15))
