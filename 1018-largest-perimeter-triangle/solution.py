class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 由大到小排序
        nums.sort(reverse=True)

        # 滑動檢視相鄰的三個數
        for i in range(len(nums) - 2):
            # nums[i] 是這三個數中的最大邊
            if nums[i + 1] + nums[i + 2] > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
                
        # 找不到任何可以組成三角形的三個數
        return 0
