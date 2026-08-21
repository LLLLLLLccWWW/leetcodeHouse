class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_one = -1   # 上一個 1 出現的索引，初始設為 -1 表示尚未出現
        for i, num in enumerate(nums):
            if num == 1:
                if last_one != -1 and i - last_one - 1 < k:
                    return False
                last_one = i
                
        return True  
