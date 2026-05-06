class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()      # 記錄視窗內有哪些字元      
        left = 0              # 視窗左邊界
        max_length = 0

        for right in range(len(s)):     # right 一直往右移
            while s[right] in char_set: # 如果右邊新字元已經在視窗內（重複了）
                char_set.remove(s[left])    # 把左邊的字元移出視窗
                left += 1                    # 左邊界往右縮
            char_set.add(s[right])              # 把新字元加入視窗
            max_length = max(max_length, right - left + 1)  # 更新最大長度
        return max_length
        
