class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        # 將所有非數字字元替換為空格
        cleaned = ''.join(c if c.isdigit() else ' ' for c in word)

        # split() 會自動過濾連續空格，int(s) 會自動去除前導零 (例如 "001" -> 1)
        seen = {int(s) for s in cleaned.split()}

        return len(seen)
