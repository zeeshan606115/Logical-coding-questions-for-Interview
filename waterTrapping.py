def maxArea(lst):
    left = 0
    right = len(lst) -1
    width = right - left
    prevarea = 0
    while left <= right:
        if lst[left] > lst[right]:
            hmax = lst[left]
            hmin = lst[right]
        else:
            hmax = lst[right]
            hmin = lst[left]
        area = width * hmin
        prevarea = max(area, prevarea)
        if hmin == lst[left]:
             
            left = left + 1
            width -= 1
        else:
            right  = right - 1
            width -=1
    print(prevarea)

maxArea([1,8,6,2,5,4,8,3,7])