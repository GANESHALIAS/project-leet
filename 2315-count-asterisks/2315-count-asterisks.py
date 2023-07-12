import collections
class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        ans=0
        for i in s:
            if i == "|":
                count+=1
            elif count%2==0:
                if i == "*":
                    ans+=1
        return ans
        