# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_height(node):
            if not node:
                return 0

            # 計算左子樹高度
            left_height = check_height(node.left)
            if left_height == -1:
                return -1   # 左子樹已經失衡，直接向上回傳 -1

            # 計算右子樹高度
            right_height = check_height(node.right)
            if right_height == -1:
                return -1   # 左子樹已經失衡，直接向上回傳 -1

            # 檢查當前節點是否失衡
            if abs(left_height - right_height) > 1:
                return -1

            # 若平衡，則回傳當前節點的實際高度
            return max(left_height, right_height) + 1

        # 如果最終結果不是 -1，代表整棵樹都是平衡的
        return check_height(root) != -1
