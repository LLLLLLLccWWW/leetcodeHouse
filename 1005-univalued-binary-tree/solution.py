# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        target_val = root.val
        def dfs(node):
            if not node:
                return True
            if node.val != target_val:
                return False
            # 左右子樹都必須符合條件
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)
