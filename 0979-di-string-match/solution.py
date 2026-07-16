class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        low = 0
        high = len(s)
        result = []

        # 遍歷字串中的每個字元
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:   # char == 'D'
                result.append(high)
                high -= 1

        # 最後 low 與 high 會相遇，將最後一個數字放進去
        result.append(low)  # 此時 low == high

        return result
