class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        i = len(num) - 1

        # 只要 num 還沒加完，或者 k 還有進位，就繼續計算
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            
            res.append(k % 10)  # 留下當前的個位數
            k //= 10            # 進位給下一位

        # 因為是從低位到高位 append，最後要反轉回來
        return res[::-1]
