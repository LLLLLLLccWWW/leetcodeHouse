# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False

        # queue 裡面存放 (當前節點, 父節點)
        queue = deque([(root,None)])
        
        while queue:
            level_size = len(queue)
            x_parent = None
            y_parent = None

            for _ in range(level_size):
                node,parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))

            # 檢查這一層的情況
            # 1. 兩者都在這一層找到 (深度相同)
            if x_parent and y_parent:
                return x_parent != y_parent     # 父節點不同才是 Cousin

            # 2. 只有其中一個在這一層找到 (深度不同)
            if x_parent or y_parent:
                return False

        return False
        
