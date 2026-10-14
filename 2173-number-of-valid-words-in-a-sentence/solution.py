class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        tokens = sentence.split()
        valid_count = 0

        for token in tokens:
            if self.is_valid(token):
                valid_count += 1

        return valid_count

    def is_valid(self,token):
        n = len(token)
        hyphen_count = 0
        punct_count = 0

        for i,ch in enumerate(token):
            # 1. 不能含有數字
            if ch.isdigit():
                return False

            # 2. 檢查連字號 '-'
            if ch == '-':
                hyphen_count += 1
                if hyphen_count > 1:
                    return False

                # 左右兩邊必須皆為小寫字母
                if i == 0 or i == n - 1 or not (token[i - 1].islower() and token[i + 1].islower()):
                    return False

            # 3. 檢查標點符號 ('!', '.', ',')
            elif ch in ('!', '.', ','):
                punct_count += 1
                if punct_count > 1:
                    return False
                # 標點符號必須位在最後一個位置
                if i != n - 1:
                    return False

        return True

