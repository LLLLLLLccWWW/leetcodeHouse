class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 步驟 1：移除所有舊的虛線，並全部轉大寫
        clean_s = s.replace('-','').upper()

        result = []
        count = 0

        # 步驟 2：從後往前遍歷字串
        for i in range(len(clean_s) - 1, -1, -1):
            result.append(clean_s[i])
            count += 1

            # 每當放滿 k 個字元，且前面還有字元時，就加一個虛線
            if count == k and i > 0:
                result.append('-')
                count = 0   # 計數器歸零，重新計算下一組

        # 步驟 3：因為是倒著放進去的，最後要反轉回來並合併成字串
        return ''.join(result[::-1])
