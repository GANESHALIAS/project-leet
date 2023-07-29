class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        if len(s)<=1:
            return len(s)
        i=1
        j=0
        length=1
        while i<len(s) and j<len(s):
            if (s[i]==s[j] or s[i] in s[j:i]) and i!=j:
                j+=1
            else:
                i+=1
            length=max(length,len(s[j:i]))
        return length