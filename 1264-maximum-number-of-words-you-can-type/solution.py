class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken_set = set(brokenLetters)
        words = text.split(' ')
        count = 0

        for word in words:
            # 檢查單字中是否有任意字元屬於損壞按鍵
            if not any(char in broken_set for char in word):
                count += 1

        return count
