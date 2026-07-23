# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(root,d):
            if not root:
                return None
            if d==len(res):
                res.append(root.val)
            dfs(root.right,d+1)
            dfs(root.left,d+1)
        dfs(root,0)
        return res