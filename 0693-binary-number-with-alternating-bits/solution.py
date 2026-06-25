class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 先取出最後一位元
        prev_bit = n % 2
        n //= 2

        while n > 0:
            current_bit = n % 2
            # 如果目前位元跟前一個位元相同，代表沒有交替
            if current_bit == prev_bit:
                return False
            prev_bit = current_bit
            n //= 2

        return True
