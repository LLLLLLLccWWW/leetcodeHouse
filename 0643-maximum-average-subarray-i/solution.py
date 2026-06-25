class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 1. 建立第一個長度為 k 的視窗總和
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # 2. 開始滑動視窗，從索引 k 開始走到最後
        for i in range(k,len(nums)):
            # 加上右邊新進來的元素 nums[i]，減去左邊離開的元素 nums[i - k]
            current_sum += nums[i] - nums[i - k]

            # 更新最大總和
            if current_sum > max_sum:
                max_sum = current_sum

        return float(max_sum) / k
