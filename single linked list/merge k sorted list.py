# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        mergelist=list()
        result=ListNode(0)
        result_tail=result
        i=0
        for i in range(0, len(lists)):
            while lists[i]:
                mergelist.append(lists[i].val)
                lists[i]=lists[i].next
            
        mergelist.sort()
        
        for t in mergelist:
            result_tail.next = ListNode(t)
            result_tail=result_tail.next
            
        return result.next
