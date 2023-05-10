class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=""
        if len(strs)==1:
            return strs[0]
        else:
            strs.sort()
            print(strs)
            x=strs[0]
            print(x)
            for i in range(0,len(x)+1):
                k=x[:i]
                print(k)
                for j in range(1,len(strs)):
                    print(strs[j])
                    if k == strs[j][:i]:
                        pass
                    else:
                        return l
                l=k
        return l