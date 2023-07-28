class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s1=str(num)
        s2=s1[::-1]
        s3=int(s2)
        s4=str(s3)
        if s2 == s4 :
            return True
        else:
            return False