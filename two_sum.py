def twoSum(nums, target):
        min = 0
        max = len(nums)-1
        dct = [(index, value) for value, index in enumerate(nums)]

        dct.sort()
        print("dct: ",dct)

        while min<=max:
            if dct[min][0] + dct[max][0] == target:
                return (dct[min][1], dct[max][1])
            elif dct[min][0] + dct[max][0] > target:
                max = max-1
            elif dct[min][0] + dct[max][0] < target:
                min = min + 1
        

x = twoSum([3,2,4],6)
if x is not None:
    print(x)
else:
    print("Not Possible")