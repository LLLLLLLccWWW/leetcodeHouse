class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])  # 取兩位數
                result.append(chr(ord('a') + num - 1))
                i -= 3  # 往前跳三格（兩位數字+#）
            else:
                num = int(s[i])      # 取一位數
                result.append(chr(ord('a') + num - 1))
                i -= 1

        return ''.join(reversed(result))

