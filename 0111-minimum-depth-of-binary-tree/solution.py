# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        # 佇列中儲存 (當前節點, 當前深度)
        queue = deque([(root,1)])

        while queue:
            node, depth = queue.popleft()

            # 如果遇到葉子節點（左右皆空），這就是答案，立馬回傳
            if not node.left and not node.right:
                return depth

            # 將子節點加入佇列
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0
