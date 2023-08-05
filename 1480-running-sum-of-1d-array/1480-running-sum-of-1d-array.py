class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsums=[]
        for i in range(len(nums)):
            runningsums.append(sum(nums[:i+1]))
        return runningsums