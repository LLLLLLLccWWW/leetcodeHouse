class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. 將字串複製兩份拼接
        # 2. 用 [1:-1] 砍掉最前面與最後面的字元
        # 3. 檢查原本的 s 是否還在這個被砍過頭尾的字串中
        return s in (s + s)[1:-1]
