from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 步驟 1：建立雜湊表，統計每個字元出現的次數
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # # 一行搞定次數統計
        # char_count = Counter(s)

        # 尋找第一個次數為 1 的字元索引
        for i,char in enumerate(s):
            if char_count[char] == 1:
                return i

        return -1
