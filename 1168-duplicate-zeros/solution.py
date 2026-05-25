class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        result = []

        for num in arr:
            result.append(num)
            if num == 0:
                result.append(0)    # 0複製一個

        # 把前n個複製回arr
        for i in range(len(arr)):
            arr[i] = result[i]
