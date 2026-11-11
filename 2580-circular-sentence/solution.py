class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # 1. 檢查首尾字元是否相等
        if sentence[0] != sentence[-1]:
            return False

        # 2. 掃描中間空格，比對相鄰單字的首尾字元
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                if sentence[i - 1] != sentence[i + 1]:
                    return False

        return True
