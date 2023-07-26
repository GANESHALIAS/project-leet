class Solution:
    def largestDivisibleSubset(self, n: List[int]) -> List[int]:
        n.sort()
        div_count=[1]*len(n)
        prev_element=[-1]*len(n)
        max_ind=0

        for z in range(len(n)):
            for y in range(z):
                if n[z]%n[y]==0:
                    if div_count[z]<div_count[y]+1:
                        div_count[z]=div_count[y]+1
                        prev_element[z]=y
                
            if div_count[max_ind]<div_count[z]:
                max_ind=z

        k=max_ind
        l=[]
        while k>=0:
            l.append(n[k])
            k=prev_element[k]
        return l
