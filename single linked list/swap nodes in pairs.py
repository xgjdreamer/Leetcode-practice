# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        listhead=list()
        i=0
        result=ListNode(0)
        result_tail=result
        while head:
            listhead.append(head.val)
            head=head.next
       
        if (len(listhead)%2==0):
            while i<len(listhead):
                q=listhead[i]
                listhead[i]=listhead[i+1]
                listhead[i+1]=q
                i=i+2
        else:
            while i<len(listhead)-1:
                q=listhead[i]
                listhead[i]=listhead[i+1]
                listhead[i+1]=q
                i=i+2
                
            
            
        for i in listhead:
            result_tail.next=ListNode(i)
            result_tail=result_tail.next
            
        return result.next
