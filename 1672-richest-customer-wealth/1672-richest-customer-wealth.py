class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum=0
        for i in range(len(accounts)):
            k=sum(accounts[i])
            if k>maxsum:
                maxsum=k
        return maxsum