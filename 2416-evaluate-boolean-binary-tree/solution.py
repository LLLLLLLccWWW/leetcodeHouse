# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        # 1. 葉子節點直接回傳布林值 (0 -> False, 1 -> True)
        if not root.left:
            return root.val == 1

        # 2. 遞迴計算左右子樹結果
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        # 3. 根據當前節點運算子進行邏輯運算 (2: OR, 3: AND)
        if root.val == 2:
            return left_val or right_val
        else:
            return left_val and right_val

