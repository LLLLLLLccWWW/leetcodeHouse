class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total = 0
        for length in range(1, n + 1, 2):   # 只考慮奇數長度
            for start in range(n - length + 1):
                total += sum(arr[start:start + length])
        return total
