# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        visited = set()

        def dfs(node):
            if not node:
                return False

            # 檢查目標配對數字是否已經出現過
            if k - node.val in visited:
                return True

            # 記錄當前數字
            visited.add(node.val)

            # 繼續往左右子樹尋找
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
