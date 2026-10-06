class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        max_num = max(nums)

        # 輾轉相除法 (Euclidean Algorithm)
        while min_num:
            max_num,min_num = min_num,max_num % min_num

        return max_num
