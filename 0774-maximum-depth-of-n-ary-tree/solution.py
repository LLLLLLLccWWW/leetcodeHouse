"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # 基礎情況：空樹的深度為 0
        if not root:
            return 0

        # 基礎情況：沒有子節點的葉子節點，深度為 1
        if not root.children:
            return 1
        
        # 遞迴計算：1 + 所有子節點深度的最大值
        return 1 + max(self.maxDepth(child) for child in root.children)
