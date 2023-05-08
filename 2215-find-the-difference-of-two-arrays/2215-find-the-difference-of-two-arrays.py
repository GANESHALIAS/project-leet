class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> List[List[int]]:
        
        k=[[],[]]
        for i in nums1:
            if i not in nums2 and i not in k[0]:
                k[0].append(i)
        for j in nums2:    
            if j not in nums1 and j not in k[1]:
                k[1].append(j)
        return k     