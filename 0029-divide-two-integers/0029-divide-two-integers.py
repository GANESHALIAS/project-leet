class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 :
            return 0
        neg=1
        if dividend<0 and divisor<0:
            neg=1
        elif dividend<0 or divisor<0:
            neg=-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        ans=len(range(0,dividend-divisor+1,divisor))*neg
        ans = min(max(ans,-2147483648),2147483647)
        return ans