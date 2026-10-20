class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. 拆分奇數與偶數索引元素
        evens = nums[::2]
        odds = nums[1::2]

        # 2. 獨立排序
        evens.sort()    # 偶數索引：非遞減 (升序)
        odds.sort(reverse=True)     # 奇數索引：非遞增 (降序)

        # 3. 重新交錯組合
        res = [0] * len(nums)
        res[::2] = evens
        res[1::2] = odds

        return res
