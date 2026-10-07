class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        # 尋找 ch 第一次出現的位置
        idx = word.find(ch)

        # 若找不到，直接回傳原字串
        if idx == -1:
            return word

        # 翻轉前綴部分並拼接剩餘字串
        return word[:idx + 1][::-1] + word[idx + 1:]
