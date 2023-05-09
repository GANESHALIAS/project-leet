class Solution:
    def isPalindrome(self, x: int) -> bool:
        k=str(x)
        l=str(x)[::-1]
        if k==l:
            return True
        else:
            return False