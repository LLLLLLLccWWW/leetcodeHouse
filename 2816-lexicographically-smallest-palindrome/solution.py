class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)
        left,right = 0, len(chars) - 1

        while left < right:
            if chars[left] < chars[right]:
                chars[right] = chars[left]
            else:
                chars[left] = chars[right]

            left += 1
            right -= 1
        
        return "".join(chars)
