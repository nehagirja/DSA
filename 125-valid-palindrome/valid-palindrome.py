class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        string = s.lower() # O(n)

        left, right = 0, len(s)-1

        # O(n)
        while left < right:
            if not string[left].isalnum():
                left += 1
                continue
            if not string[right].isalnum():
                right -= 1
                continue
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

# total time complexity = O(n)
#  and space is O(n)        

        

    