class Solution:
    

    def validPalindrome(self, s: str) -> bool:
            st=0
            en=len(s)-1
            while st<=en:
                if s[st] != s[en]:
                    str1 = s[:st]+s[st+1:]
                    str2 = s[:en]+s[en+1:]
                    return str1==str1[::-1] or str2==str2[::-1]
                st+=1
                en-=1
            return True