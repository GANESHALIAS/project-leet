class Solution:
    def isValid(self, s: str) -> bool:
        store={"(":")","{":"}","[":"]"}
        ans=[]
        for i in s:
            if i in store:
                ans.append(i)
            elif len(ans) == 0 or store[ans.pop()] != i:
                return False
        return len(ans)==0