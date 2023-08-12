class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k=pow(num,0.5)
        m=int(k)
        if m == k:
            return True
        else:
            return False