# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # 兩個都是空的 → 相同
        if not p and not q:
            return True
        # 其中一個是空的 → 不同
        if not p or not q:
            return False
        # 當前節點值不同 → 不同
        if p.val != q.val:
            return False
        
        # 遞迴比較左子樹和右子樹
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
