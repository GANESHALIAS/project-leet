class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_c=collections.Counter(s)
        t_c=collections.Counter(t)
        for i in t_c:
            if t_c[i]!=s_c[i]:
                return False
        return True