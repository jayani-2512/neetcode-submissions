# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=head
        for i in range(left-1):
            prev,curr=curr,curr.next

        pprev=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=pprev
            pprev=curr
            curr=temp
        prev.next.next=curr
        prev.next=pprev
        return dummy.next
