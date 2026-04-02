class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 #max window possible
        l = 0 #left
        maxf = 0  #this is the frequency of the most occuring variable

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #adding to the hashmap 
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k: #imp
                count[s[l]] -= 1
                l += 1 #this is where we shrink the window 
            res = max(res, r - l + 1) #existing vs the window size 
        return res 

#this is a hard problem, it just says its medium. it is important to not the while loop. 