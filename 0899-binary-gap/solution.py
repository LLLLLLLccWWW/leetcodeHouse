class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_gap = 0
        last_pos = None
        curr_pos = 0

        while n > 0:
            # 檢查最低位是否為1
            if n & 1:
                if last_pos is not None:
                    max_gap = max(max_gap, curr_pos - last_pos)
                last_pos = curr_pos

            n >>= 1 # 右移一位
            curr_pos += 1   # 位元索引 +1
            
        return max_gap
            
