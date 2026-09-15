class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)

        for i in range(n):
            # 檢查當前元素是否大於下一個元素（包含尾端接回頭部的狀況）
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False

        return True

