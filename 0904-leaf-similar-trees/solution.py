# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import izip_longest
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def yield_leaves(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            else:
                # Python 2 不支援 yield from，改用傳統 for 迴圈
                for leaf in yield_leaves(node.left):
                    yield leaf
                for leaf in yield_leaves(node.right):
                    yield leaf

        for l1,l2 in izip_longest(yield_leaves(root1),yield_leaves(root2)):
            if l1 != l2:
                return False

        return True
