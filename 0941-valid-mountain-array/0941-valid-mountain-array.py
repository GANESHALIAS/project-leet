class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_e=max(arr)
        max_i=arr.index(max_e)
        if max_i == 0 or max_i == len(arr)-1:
            return False
        i=1
        while i <= max_i:
            if arr[i] <= arr[i-1]:
                print("w1",i)
                return False
            i+=1
        print("end1")
        i=max_i+1
        while i<len(arr):
            if arr[i] >= arr[i-1]:
                print(i)
                return False
            i+=1
        return True