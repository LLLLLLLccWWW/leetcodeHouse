class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) > 1:
            # 走訪新陣列的每個索引 i
            # 偶數 i 取 min，奇數 i 取 max
            nums = [
                min(nums[2*i],nums[2*i+1]) if i % 2 == 0
                else max(nums[2*i],nums[2*i+1])
                for i in range(len(nums) // 2)
            ]

        return nums[0]
