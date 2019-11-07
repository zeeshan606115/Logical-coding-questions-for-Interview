def zeroAtEnd(number):
	for i in number:
		if i == 0:
			number.remove(0)
			number.append(0)
	return number

numbers = input("Enter multiple number with space: ")
numbers = numbers.split()
numbers = list(map(int, numbers))
s = zeroAtEnd(numbers)
print(s)