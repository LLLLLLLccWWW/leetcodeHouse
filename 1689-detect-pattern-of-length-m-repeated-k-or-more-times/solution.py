class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        n = len(arr)

        for i in range(n - m * k + 1):
            if all(arr[i + j] == arr[i + j + m] for j in range(m * (k - 1))):
                return True

        return False
