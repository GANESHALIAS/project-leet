class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=int(str(x)[::-1])
        else:
            x=int(str(x)[1:][::-1])*-1
        if x>2147483648 or x<-2147483648:
            return 0
        else:
            return x
