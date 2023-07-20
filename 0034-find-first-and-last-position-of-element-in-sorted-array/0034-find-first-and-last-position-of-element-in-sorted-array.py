class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f=-1
        l=-1
        i=0
        j=len(nums)-1
        while i<len(nums) and j>=i :
            if nums[i]==target:
                f=i
            else:
                i+=1
            if nums[j]==target:
                l=j
            else:
                j-=1
            if f!=-1 and l!=-1:
                break
        return [f,l]