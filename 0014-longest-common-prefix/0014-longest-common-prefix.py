class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=""
        for i in range(1,len(strs[0])+1):
            k=strs[0][:i]
            for j in strs:
                if k == j[:i]:
                    pass
                else:
                    return l
            l=k
        return l