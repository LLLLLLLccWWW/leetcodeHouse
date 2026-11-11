class Solution:
    def averageValue(self, nums: list[int]) -> int:
        # 既是偶數又能被 3 整除 <=> 能被 6 整除
        valid_nums = [x for x in nums if x % 6 == 0]

        if not valid_nums:
            return 0

        return sum(valid_nums) // len(valid_nums)
