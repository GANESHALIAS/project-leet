class Solution:
    def addDigits(self, num: int) -> int:
        s=list(str(num))
        while len(s)!=1:
            s=list(map(int,s))
            s=sum(s)
            s=str(s)
        print(s)
        return int(s[0])