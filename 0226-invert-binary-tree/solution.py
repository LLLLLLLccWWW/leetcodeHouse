# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 基底條件：如果是空節點，直接回傳
        if not root:
            return None

        # 暫存原本的左子樹與右子樹（因為接下來會被覆蓋
        left_side = root.left
        right_side = root.right

        # 互相交換，並遞迴下去翻轉子樹
        root.left = self.invertTree(right_side)
        root.right = self.invertTree(left_side)

        return root
