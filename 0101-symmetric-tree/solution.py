# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(left,right):
            if not left and not right:  # 兩邊都空 → 對稱
                return True
            if not left or not right:   # 只有一邊空 → 不對稱
                return False
            
            return (left.val == right.val and          # 當前值相同
                    isMirror(left.left, right.right) and  # 外側對稱
                    isMirror(left.right, right.left))     # 內側對稱
        return isMirror(root.left,root.right)
        
