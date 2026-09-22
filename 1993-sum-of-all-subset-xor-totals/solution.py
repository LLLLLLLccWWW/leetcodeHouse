from functools import reduce
import operator
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 將所有數字進行 OR 運算後乘以 2^(N-1)
        or_sum = reduce(operator.or_,nums)
        return or_sum << (len(nums) - 1)
