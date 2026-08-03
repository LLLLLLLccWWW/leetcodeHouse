"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            # 正序將子節點放入 stack (出棧時會變成右至左處理)
            if node.children:
                stack.extend(node.children)
                
        # 反轉結果即為後序走訪：[Left -> Right -> Root]
        return res[::-1]
