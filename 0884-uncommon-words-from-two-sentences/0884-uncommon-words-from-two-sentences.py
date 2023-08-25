class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=list(s1.split())+list(s2.split())
        ans_c=collections.Counter(ans)
        p=[]
        for i in ans_c:
            if ans_c[i]==1:
                p.append(i)
        return p