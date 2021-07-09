def three_sum(lst):
    lst.sort()
    l = []
    for i in range(len(lst)-2):
        if i== 0 or (lst[i] != lst[i-1]):
            low = i + 1
            high= len(lst)-1
            sum = 0 - lst[i]
            while (low < high):
                if lst[low] + lst[high] == sum:
                    print(lst[i], lst[low], lst[high])
                    l.append([lst[i], lst[low], lst[high]])
                    while low < high and lst[low] == lst[low + 1]:
                        low +=1
                    while low <high and lst[high] == lst[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                else:
                    if lst[low] + lst[high] < sum:
                        low += 1
                    else:
                        high -= 1
    return l

print(three_sum([-2,-2, -1, -1, 0,0,0 ,1,1,2,2]))