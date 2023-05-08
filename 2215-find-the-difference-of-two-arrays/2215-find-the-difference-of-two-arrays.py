class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        k=[[],[]]
        for i in nums1:
            if i not in nums2:
                k[0].append(i)
        for j in nums2:    
            if j not in nums1:
                k[1].append(j)
        k[0]=list(set(k[0]))
        k[1]=list(set(k[1]))
        return k     