class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 壓縮去除連續重複的數字
        compressed = [nums[0]]
        for x in nums[1:]:
            if x != compressed[-1]:
                compressed.append(x)

        count = 0
        # 2. 檢查去重後的陣列（兩端點不可能為 Hill/Valley）
        for i in range(1,len(compressed) - 1):
            left,mid,right = compressed[i - 1],compressed[i],compressed[i + 1]
            # 同時大於兩側 (Hill) 或 同時小於兩側 (Valley)
            if (mid > left and mid > right) or (mid < left and mid < right):
                count += 1

        return count
