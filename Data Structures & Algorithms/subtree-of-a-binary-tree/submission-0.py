# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root :
            return False
        if not subRoot:
            return True

        def same(root,subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val==subRoot.val:
                return (same(root.left,subRoot.left) and same(root.right,subRoot.right))
            return False

        if same(root,subRoot):
            return True
        left=self.isSubtree(root.left,subRoot)
        right=self.isSubtree(root.right,subRoot)
        return left or right