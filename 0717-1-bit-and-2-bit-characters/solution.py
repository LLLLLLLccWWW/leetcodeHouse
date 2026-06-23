class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)

        # 掃描到倒數第二個元素即可（因為我們要看能不能剛好停在最後一個元素）
        while i < n - 1:
            if bits[i] == 1:
                i += 2  # 遇到 1，強迫跟後面湊成 2 位元字元，跳 2 步
            else:
                i += 1  # 遇到 0，獨立字元，跳 1 步

        # 如果最後指標 i 剛好停在 n - 1 的位置，說明最後一個字元是獨立的 1-bit 字元
        return i == n - 1
