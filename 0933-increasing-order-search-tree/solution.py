# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dummy = TreeNode(0)
        self.curr = dummy

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            node.left = None
            self.curr.right = node
            self.curr = node

            inorder(node.right)

        inorder(root)
        return dummy.right
