# We will rotate array after specific position
import sys

def arrayRotation(l, num):
	if n > len(l):
		print("Your entered value is greater than the length of Array!!")
		sys.exit()

	else:
		for i in range(n):
			x = l.pop(0)
			l.append(x)
		return l


l = [1,2,9,8,11,56,43,79]
print(l)
n = int(input("enter the value where you want to split: "))
x = arrayRotation(l,n)
print(x)
