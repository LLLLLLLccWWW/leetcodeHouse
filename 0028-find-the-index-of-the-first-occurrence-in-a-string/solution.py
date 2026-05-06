class Solution(object):
    # 從 haystack 的每個位置開始，切出跟 needle 一樣長的子字串來比對。
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)   # needle 的長度，用來決定每次切多長

        # len(haystack) - n + 1 確保切片不會超出範圍
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:   # 從 i 開始切出跟 needle 一樣長的子字串來比對
                return i    # 找到了，回傳起始位置
        return -1   # 跑完都沒找到，回傳 -1
        
