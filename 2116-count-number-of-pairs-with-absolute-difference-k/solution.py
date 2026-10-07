from collections import Counter
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter()
        count = 0

        for num in nums:
            # 尋找左側符合 num - k 或 num + k 的數字個數
            count += freq[num - k] + freq[num + k]
            # 將當前數字加入頻率表
            freq[num] += 1

        return count
