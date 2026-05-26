# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right,low,high)    # 只找右邊
        
        if root.val > high:
            return self.rangeSumBST(root.left,low,high)    # 只找左邊
        
        # 在範圍內，左右都找
        return root.val + self.rangeSumBST(root.right,low,high) + self.rangeSumBST(root.left,low,high)

        
