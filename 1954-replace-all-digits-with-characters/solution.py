class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)

        # 走訪所有奇數索引
        for i in range(1,len(s_list),2):
            prev_char = s_list[i - 1]
            shift_val = int(s_list[i])

            # 計算偏移後的字元
            s_list[i] = chr(ord(prev_char) + shift_val)

        return "".join(s_list)
