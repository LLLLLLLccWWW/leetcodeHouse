from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)

        # 只加總出現次數為 1 的數字
        return sum(num for num,count in counts.items() if count == 1)
