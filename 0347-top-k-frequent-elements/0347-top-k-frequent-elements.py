import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=collections.Counter(nums)
        s=set(nums)
        ans=sorted(c.items(), key=lambda x:x[1], reverse=True)
        r=[]
        for i in range(k):
            r.append(ans[i][0])
        return r