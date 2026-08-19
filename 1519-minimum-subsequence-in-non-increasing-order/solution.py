class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        total = sum(nums)
        current_sum = 0
        result = []

        for num in nums:
            current_sum += num
            result.append(num)
            if current_sum > total - current_sum:
                break

        return result
