def getMax(lst):
    sum = 0
    max1 = lst[0]
    for i in range(len(lst)):
        sum += lst[i]
        max1 = max(sum, max1)
        if sum < 0:
            sum = 0
        # if sum > max:
        #     max = sum
         
    print(max1)

getMax([-2,1,-3,4,-1,2,1,-5,4])