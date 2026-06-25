# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 初始化變數
        self.result = []
        self.prev_val = None
        self.current_count = 0
        self.max_count = 0

        def inorder(node):
            if not node:
                return

            # 1. 走訪左子樹
            inorder(node.left)

            # 2. 處理當前節點（核心邏輯）
            if node.val == self.prev_val:
                self.current_count += 1
            else:
                self.current_count = 1
                self.prev_val = node.val

            # 檢查是否更新眾數
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.result = [node.val]     # 發現新霸主，清空舊答案
            elif self.current_count == self.max_count:
                self.result.append(node.val) # 次數相同，並列眾數

            # 3. 走訪右子樹
            inorder(node.right)

        # 開始中序走訪
        inorder(root)
        return self.result
