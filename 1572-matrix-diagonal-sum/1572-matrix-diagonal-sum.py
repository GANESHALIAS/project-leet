class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]+mat[i][len(mat[i])-1-i]
            print(mat[i][i],mat[i][len(mat[i])-1-i])
        if len(mat)%2 != 0:
            k=len(mat)//2
            s-=mat[k][k]
        return s