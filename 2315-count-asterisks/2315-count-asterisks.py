import collections
class Solution:
    def countAsterisks(self, s: str) -> int:
        k=s.split("|")
        i=1
        while i<len(k):
            k[i]=""
            i+=2
        k="".join(k)
        c=collections.Counter(k)
        
        return c["*"]
        