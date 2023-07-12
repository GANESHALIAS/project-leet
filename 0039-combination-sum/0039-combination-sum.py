class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        st = []
        def getcombination(ind,target):
            if target == 0:
                ans.append(st[:])
                return
            if ind == len(candidates):
                return
            if candidates[ind]<=target:
                st.append(candidates[ind])
                getcombination(ind,target-candidates[ind])
                st.pop()
            getcombination(ind+1,target)
        getcombination(0,target)
        return ans