class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        ds=[]

        def getcombination(ind,n):
            if n == 0 and len(ds) == k:
                ans.append(ds[:])
                return
            
            if len(ds) == k or ind == 10 or n<=0:
                return
            
            if ind<=n and ind not in ds:
                ds.append(ind)
                getcombination(ind,n-ind)
                ds.pop()
            getcombination(ind+1,n)
        
        getcombination(1,n)
        return ans

    