# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node,is_left):
            if not node:
                return 0
            
            # 是葉節點（沒有子節點）
            if not node.left and not node.right:
                return node.val if is_left else 0   # 是左葉才加
            # 繼續往下找，左子節點傳True，右子節點傳False
            return dfs(node.left,True) + dfs(node.right,False)
        
        return dfs(root,False)  # root 不是左子節點
        
