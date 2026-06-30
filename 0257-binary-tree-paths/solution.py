# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []

        def dfs(node,current_path):
            if not node:
                return

            # 將當前節點加入路徑
            if current_path:
                current_path += "->" + str(node.val)
            else:
                current_path = str(node.val)

            # 如果是葉子節點，將這條完整的路徑存入結果
            if not node.left and not node.right:
                result.append(current_path)
                return

            # 如果不是葉子，繼續往左、右子樹探索
            if node.left:
                dfs(node.left,current_path)
            if node.right:
                dfs(node.right,current_path)

        # 從根節點開始，初始路徑為空字串
        dfs(root,"")
        return result
