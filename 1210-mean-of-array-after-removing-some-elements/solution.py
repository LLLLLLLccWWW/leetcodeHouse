class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        n = len(arr)
        remove_count = n // 20  # 5% 的元素個數

        trimmed = arr[remove_count : n - remove_count]
        return float(sum(trimmed)) / len(trimmed)
