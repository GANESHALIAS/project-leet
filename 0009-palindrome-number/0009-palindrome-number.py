class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            l=int(str(x)[::-1])
            if x==l:
                return True
            else:
                return False
        else:
            return False