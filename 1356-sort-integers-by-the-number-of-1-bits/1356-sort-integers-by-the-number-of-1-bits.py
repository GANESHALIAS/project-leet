class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)):
            k=bin(arr[i])
            k=k.replace("0b","")
            if arr[i] != 0:
                k=k.replace("0","")
            ans.append([k,arr[i]])
        ans.sort()
        ans1=[]
        for i in ans:
            ans1.append(i[1])
        return ans1