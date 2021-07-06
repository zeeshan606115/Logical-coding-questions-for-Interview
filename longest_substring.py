
def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    length = 0 
    d = {}
    while(right < len(s)):
        if s[right] in d.keys():

            left = max(d[s[right]]+1, left)

        d[s[right]] = right
        length = max(length, right-left +1)
        right+=1
    return  length


print(lengthOfLongestSubstring("dvdf"))