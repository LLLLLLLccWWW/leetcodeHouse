from collections import Counter
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # 把非字母的字元換成空格，轉小寫，切割成單字
        words = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
        
        banned_set = set(banned)  # 轉成set，查詢更快
        
        # 計算不在banned裡的字的次數
        count = Counter(w for w in words if w not in banned_set)
        
        return count.most_common(1)[0][0]  # 回傳出現最多次的字
