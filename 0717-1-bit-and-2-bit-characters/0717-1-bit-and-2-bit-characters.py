class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits.pop()
        bits=bits[::-1]
        bits=[ str(i) for i in bits]
        s="".join(bits)
        s=s.replace("11","")
        s=s.replace("01","")
        if len(s)!=0:
            if "1" in s:
                return False
            else:
                return True
        else:
            return True