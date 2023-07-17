# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s1=[]
        
        while list1 != None:
            s1.append(list1.val)
            list1=list1.next
        while list2 != None:
            s1.append(list2.val)
            list2=list2.next
        s1.sort()
        dummy = sum_num = ListNode()
        i=0
        while i<len(s1):
            if sum_num.next:
                sum_num = sum_num.next
            else:
                sum_num.next = ListNode()
                sum_num = sum_num.next
            sum_num.val =  s1[i]
            i+=1
        
        return dummy.next