# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        curr=head
        while curr:
            n+=1
            curr=curr.next
        dummy=ListNode(0,head)
        prevg=dummy
        
        while n>=k:
            kth=prevg
            for _ in range(k):
                kth=kth.next
            nextg=kth.next
            prev=nextg
            curr=prevg.next
            while curr!=nextg:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            first=prevg.next
            prevg.next=kth
            prevg=first
            n-=k
        return dummy.next