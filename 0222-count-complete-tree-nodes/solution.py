# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        # 計算最左側高度
        left_height = 0
        left_node = root
        while left_node:
            left_height += 1
            left_node = left_node.left

        # 計算最右側高度
        right_height = 0
        right_node = root
        while right_node:
            right_height += 1
            right_node = right_node.right

        # 如果左右高度相等，說明是滿二元樹，直接用公式計算
        # 這裡的高度包含根節點，所以節點數為 (1 << left_height) - 1
        if left_height == right_height:
            return (1 << left_height) - 1

        # 如果不相等，遞迴計算：根節點(1) + 左子樹節點數 + 右子樹節點數
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
