class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        l=[pref[0]]
        for i in range(1,len(pref)):
            k=pref[i-1]^pref[i]
            l.append(k)
        return l