from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)

        # 逐一嘗試刪除 index i 的字元
        for i in range(n):
           # 建立刪除第 i 個字元後的字串 
           sub_word = word[:i] + word[i + 1:]

           # 統計剩餘字元的頻率
           counts = Counter(sub_word)
           # 若所有字元頻率都相等（Set 長度為 1），即符合條件
           if len(set(counts.values())) == 1:
            return True

        return False

