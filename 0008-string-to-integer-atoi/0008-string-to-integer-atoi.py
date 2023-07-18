class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0     
        k=""
        n=1
        if s[0].isalpha():
            return 0
        else:
            n=0
            p=0
            num=0
            for i in range(len(s)):
                if s[i] == "-" and (n or p or num) == 0:
                    n=-1
                elif s[i]== "+" and (n or p or num) == 0:
                    n=1
                elif s[i].isnumeric():
                    k+=s[i]
                    num=1
                else:
                    if num==1:
                        break
                    else:                    
                        return 0
        if len(k)==0:
            return 0
        k=int(k)
        if n:
            k=k*n
        if k>2147483647:
            return 2147483647
        elif k<-2147483648:
            return -2147483648
        return k
                    
        