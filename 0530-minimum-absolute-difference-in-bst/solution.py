# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 初始化為無窮大，用來儲存最小差值
        self.min_diff = float('inf')
        # 用來記錄中序走訪時的「前一個節點值
        self.prev = None

        def inorder(node):
            if not node:
                return

            # 1. 先走訪左子樹
            inorder(node.left)

            # 2. 處理當前根節點
            if self.prev is not None:
                # 計算當前節點與前一個節點的差值，並更新全域最小值
                self.min_diff = min(self.min_diff,node.val - self.prev)

            # 更新 prev 為當前節點值，供下一個節點比較使用
            self.prev = node.val

            # 3. 最後走訪右子樹
            inorder(node.right)

        # 從根節點開始中序走訪
        inorder(root)

        return self.min_diff
