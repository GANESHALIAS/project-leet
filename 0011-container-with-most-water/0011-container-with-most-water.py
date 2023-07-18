class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        p1=0
        p2=len(height)-1
        while p2>p1:
            l=p2-p1
            if height[p2]>height[p1]:
                ans=max(l*height[p1],ans)
                p1+=1
            else:
                ans=max(l*height[p2],ans)
                p2-=1
        return ans
        