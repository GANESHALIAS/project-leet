import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b=0
        c=0
        s_c=collections.Counter(secret)
        g_c=collections.Counter(guess)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                b+=1
        k=0
        for i in s_c:
            k+=min(s_c[i],g_c[i])
        c=k-b
        return str(b)+"A"+str(c)+"B"