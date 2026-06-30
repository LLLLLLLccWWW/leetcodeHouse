class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        while columnNumber > 0:
            # 關鍵步驟：先減 1，將 1-26 對應轉換成 0-25
            columnNumber -= 1

            # 取得當前最低位的字元餘數
            remainder = columnNumber % 26

            # 將 0-25 轉換為 'A'-'Z' 並加入 result
            result.append(chr(ord('A') + remainder))

            # 往高位進階
            columnNumber //= 26

        # 因為我們是從低位（個位數）開始算，最後要把結果反轉過來
        return "".join(reversed(result))
