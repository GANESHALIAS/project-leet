import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=collections.Counter(arr)
        ans=[]
        s=set()
        for i in c:
            ans.append(c[i])
            s.add(c[i])
        return len(ans) == len(s)
            