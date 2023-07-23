class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        l=[]
        for i in range(len(pref)):
            if l :
                l.append(pref[i-1]^pref[i])
            else:
                l.append(pref[i])
        return l