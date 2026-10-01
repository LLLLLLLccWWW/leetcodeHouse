class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 1. 將字串轉換為對應字母位置的數字字串
        digits_str = "".join(str(ord(char) - ord('a') + 1) for char in s)

        # 2. 進行第一次位數求和
        current_sum = sum(int(digit) for digit in digits_str)

        # 3. 重複變換操作 k - 1 次
        for _ in range(k - 1):
            next_sum = 0
            while current_sum > 0:
                next_sum += current_sum % 10
                current_sum //= 10

            current_sum = next_sum

        return current_sum
        
