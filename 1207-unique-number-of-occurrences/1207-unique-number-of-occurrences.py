import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=collections.Counter(arr)
        ans=[]
        for i in c:
            ans.append(c[i])
        if len(ans) == len(set(ans)):
            return True
        else:
            return False