class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # start ^ goal 找出相異的 bit，再計算 1 的數量
        return (start ^ goal).bit_count()
        
