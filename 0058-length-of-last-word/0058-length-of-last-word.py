class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        k=s[::-1]
        for i in range(len(k)):
            if k[i]==" ":
                return i
        return len(k)