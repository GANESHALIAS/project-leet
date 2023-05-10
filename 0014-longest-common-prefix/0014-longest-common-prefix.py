class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=""
        x=strs[0]
        for i in range(0,len(x)+1):
            k=x[:i]
            for j in range(1,len(strs)):
                if k == strs[j][:i]:
                    pass
                else:
                    return l
            l=k
        return l