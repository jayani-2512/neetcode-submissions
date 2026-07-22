# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def level(root,d):
            #nonlocal res
            if not root:
                return None
            if len(res)==d:
                res.append([])
            res[d].append(root.val)
            level(root.left,d+1)
            level(root.right,d+1)
        level(root,0)
        return res
            
            

