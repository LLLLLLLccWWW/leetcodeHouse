class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        threshold = len(arr) // 4
        count = Counter(arr)

        for num, cnt in count.items():
            if cnt > threshold:
                return num
