class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum= sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # 檢查左側總和是否等於右側總和 (total_sum - left_sum - num)
            if left_sum == total_sum - left_sum - num:
                return i 
            left_sum += num

        return -1
