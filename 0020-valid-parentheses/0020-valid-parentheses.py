class Solution:
    def isValid(self, s: str) -> bool:
        store={"(":")","{":"}","[":"]"}
        k=[]
        for i in s:
            if i in store:
                k.append(i)
            elif len(k) == 0 :
                return False
            elif store[k.pop()] != i:
                return False
        return len(k)==0