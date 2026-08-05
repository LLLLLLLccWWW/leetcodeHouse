# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total_tilt = 0

        def calculate_sum(node):
            if not node:
                return 0

            # 後序遍歷：先拿到左右子樹各自的總和
            left_sum = calculate_sum(node.left)
            right_sum = calculate_sum(node.right)

            # 累加當前節點的傾斜度
            self.total_tilt += abs(left_sum - right_sum)

            # 傳回包含當前節點的整棵子樹總和
            return left_sum + right_sum + node.val

        calculate_sum(root)
        return self.total_tilt
