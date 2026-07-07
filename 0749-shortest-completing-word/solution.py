from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # 1. 統計車牌中所有英文字母的小寫頻率
        target_counts = Counter(c.lower() for c in licensePlate if c.isalpha())

        best_word = None

        # 2. 依序檢查 words 裡面的每一個單字
        for word in words:
            word_counts = Counter(word)

            # 檢查當前單字是否包含車牌的所有字母（數量也要夠
            is_completing = True
            for char, count in target_counts.items():
                if word_counts[char] < count:
                    is_completing = False
                    break

            # 3. 如果符合條件，再檢查它是不是目前最短的
            if is_completing:
                if best_word is None or len(word) < len(best_word):
                    best_word = word

        return best_word
