class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f=[]
        k=0
        for i in range(len(nums)):
            k+=i*nums[i]
        f.append(k)
        nums=nums[::-1]
        s=sum(nums)
        for i in range(len(nums)):
            nums_pop=nums[i]
            p=f[-1]+(s-nums_pop)-(nums_pop*(len(nums)-1))
            f.append(p)
        return max(f)
        