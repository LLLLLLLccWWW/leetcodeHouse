# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:  # 一直往左走，沿途推入stack
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()  # 左邊走完，取出節點
            result.append(curr.val) # 記錄這個節點
            curr = curr.right   # 往右走
        return result
