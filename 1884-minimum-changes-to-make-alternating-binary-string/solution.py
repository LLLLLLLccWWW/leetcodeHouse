class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_pattern_a = 0 # 記錄符合 "0101..." 所需的修改次數

        for i,char in enumerate(s):
            # 模式 A: 偶數索引期望是 '0'，奇數索引期望是 '1'
            expected_char = '0' if i % 2 == 0 else '1'
            if char != expected_char:
                count_pattern_a += 1

        n = len(s)

        # 模式 B 所需的修改次數即為 n - count_pattern_a
        return min(count_pattern_a, n - count_pattern_a)
