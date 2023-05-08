class Solution:
    def findDifference(self, nums1: set[int], nums2: set[int]) -> List[List[int]]:
        nums1=set(nums1)
        nums2=set(nums2)
        k=[[],[]]
        for i in nums1:
            if i not in nums2:
                k[0].append(i)
        for j in nums2:    
            if j not in nums1:
                k[1].append(j)
        
        return k     