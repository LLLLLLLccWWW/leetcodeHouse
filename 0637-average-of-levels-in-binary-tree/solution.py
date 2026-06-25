# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []

        result = []
        queue = deque([root])   # 初始化佇列，將根節點放入

        while queue:
            level_size = len(queue) # 當前層的節點數量
            level_sum = 0

            # 精準取出當前層的所有節點
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # 將下一層的子節點放入佇列中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 計算平均值並加入結果
            result.append(float(level_sum) / level_size)

        return result
