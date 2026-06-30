from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 統計每個數字出現的次數
        counts = Counter(nums)
        max_length = 0

        # 2. 遍歷哈希表中的每一個數字
        for num in counts:
            # 檢查比當前數字大 1 的數字是否存在
            if num + 1 in counts:
                # 如果存在，計算兩者次數相加，並更新最大長度
                current_length = counts[num] + counts[num + 1]
                max_length = max(max_length,current_length)

        return max_length
