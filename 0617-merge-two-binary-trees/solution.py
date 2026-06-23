# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 如果其中一棵樹為空，直接回傳另一棵樹
        if not root1:
            return root2
        if not root2:
            return root1

        # 直接就地將 root2 的值加到 root1 上
        root1.val += root2.val
        
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1

        # # 如果兩者都有值，建立新節點，並把數值相加
        # merged_node = TreeNode(root1.val + root2.val)

        # # 遞迴合併左子樹與右子樹
        # merged_node.left = self.mergeTrees(root1.left, root2.left)
        # merged_node.right = self.mergeTrees(root1.right, root2.right)

        # # 回傳合併後的新節點
        # return merged_node
