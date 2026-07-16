class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # 1. 建立外星字母的權重對照表 (字母 -> 索引位置)
        order_map = {char: index for index, char in enumerate(order)}
        
        # 2. 兩兩比對相鄰的單字
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # 比對兩單字的每一個字元，長度以較短者為限
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                # 取得兩字元在外星語中的權重
                char1_order = order_map[word1[j]]
                char2_order = order_map[word2[j]]
                
                # 如果遇到不一樣的字元
                if char1_order != char2_order:
                    # 如果前者的字母權重比較大，說明沒有排好序
                    if char1_order > char2_order:
                        return False
                    # 如果前者比較小，則這兩個單字順序正確，直接跳出 inner loop 比對下一對
                    break
            else:
                # 這是 Python 特有的 for-else 語法：
                # 如果 for 迴圈正常結束（沒有遇到 break），代表其中一個單字是另一個單字的前綴。
                # 此時必須確保「較短的單字」排在前面。如果 word1 比較長，則為非法排序。
                if len(word1) > len(word2):
                    return False
                    
        return True
