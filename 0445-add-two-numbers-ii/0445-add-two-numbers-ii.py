# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_arr=[]
        l2_arr=[]
        k1=l1
        k2=l2
        
        while l2 != None:
            l2_arr.append(l2.val)
            l2=l2.next
        while l1 != None:
            l1_arr.append(l1.val)
            l1=l1.next
        
        k=len(l1_arr)-len(l2_arr)
        ans=k1
        head=ans
        if k>0:
            
            l2_arr=[0 for i in range(k)]+l2_arr
            
            ans=k1
            head=ans
        elif k<0:
            l1_arr=[0 for i in range(abs(k))]+l1_arr
            ans=k2
            head=ans
        l1_arr=l1_arr[::-1]
        l2_arr=l2_arr[::-1]
        
        for i in range(len(l1_arr)):
            l1_arr[i]+=l2_arr[i]
            if l1_arr[i]>9 and i != len(l1_arr)-1:
                l1_arr[i+1]+=1
                l1_arr[i]-=10
            elif l1_arr[i]>9 and i == len(l1_arr)-1:
                l1_arr.append(1)
                l1_arr[i]-=10
                k2=1
        print(l1_arr)
        l1_arr=l1_arr[::-1]
        i=0
        ans1=ListNode()
        dummy = sum_num = ListNode()
        while i<len(l1_arr):
            sum_num.val =  l1_arr[i]
            if sum_num.next == None and i+1<len(l1_arr):
                sum_num.next = ListNode()
                sum_num = sum_num.next
            else:
                sum_num = sum_num.next 
            i+=1
        
        return dummy