class Solution:
    def isPalindrome(self, x: int) -> bool:
        k=str(x)
        l=k[::-1]
        if k==l:
            return True
        else:
            return False