class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        # 讓數量較多（或相等）的那組先放，決定起始位置
        if len(letters) < len(digits):
            letters, digits = digits, letters

        result = []
        for i in range(len(digits)):
            result.append(letters[i])
            result.append(digits[i])
        # letters 可能比 digits 多一個，補在最後
        if len(letters) > len(digits):
            result.append(letters[-1])

        return ''.join(result)
        
