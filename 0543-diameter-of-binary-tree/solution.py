# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0

        def max_depth(node):
            if not node:
                return 0

            # 遞迴計算左子樹與右子樹的深度
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)

            # 核心：更新全域的最長直徑（左深度 + 右深度）
            self.max_diameter = max(self.max_diameter,left_depth + right_depth)

            # 回傳給上一層父節點的深度（當前節點自身算 1 層）
            return max(left_depth,right_depth) + 1

        max_depth(root)
        return self.max_diameter
