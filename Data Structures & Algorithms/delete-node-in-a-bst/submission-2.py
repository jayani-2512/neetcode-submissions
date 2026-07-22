# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # leaf node
        if not root:
            return root
        prev=None
        curr=root
        while curr and curr.val!=key:
            prev=curr
            if key<curr.val:
                curr=curr.left
            else:
                curr=curr.right
        if not curr:
            return root
        # one child or no child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not prev:
                return child
            if prev.left==curr:
                prev.left=child
            else:
                prev.right=child
        #two children
        else:
            pre=curr
            pprev=curr.left
            while pprev.right:
                pre=pprev
                pprev=pprev.right
            curr.val=pprev.val

            if pre==curr:
                pre.left=pprev.left
            else:
                pre.right=pprev.left
        return root


        
