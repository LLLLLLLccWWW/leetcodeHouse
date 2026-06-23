# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(left,right):
            # 當左邊界大於右邊界，代表這段區間已經沒有元素了，回傳 None
            if left > right:
                return None

            # 找出中間元素的索引（使用整除法防止溢位）
            mid = left + (right - left) // 2

            # 以中間元素建立目前的節點
            root=TreeNode(nums[mid])

            # 遞迴建立左子樹（區間變成左邊界到 mid - 1
            root.left = helper(left, mid - 1)

            # 遞迴建立右子樹（區間變成 mid + 1 到右邊界）
            root.right = helper(mid + 1,right)

            return root
            
        # 初始呼叫，傳入整個陣列的左右邊界索引
        return helper(0, len(nums) - 1)
