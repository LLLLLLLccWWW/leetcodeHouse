class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1  # a 的最後一位
        j = len(b) - 1  # b 的最後一位
        carry = 0
        result = ""

        while i>=0 or j>=0 or carry:
            val_a = int(a[i]) if i>=0 else 0    # a 還有數字就取，否則補0
            val_b = int(b[j]) if j>=0 else 0    # b 還有數字就取，否則補0
            total = val_a + val_b + carry
            carry = total // 2   # 二進位進位除以2
            result = str(total % 2) + result

            i-=1
            j-=1

        return result
