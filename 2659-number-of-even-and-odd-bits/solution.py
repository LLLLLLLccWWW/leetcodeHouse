class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        # 0x5555 = 0101010101010101_2 (所有偶數位為 1)
        # 0xAAAA = 1010101010101010_2 (所有奇數位為 1)
        return [(n & 0x5555).bit_count(),(n & 0xAAAA).bit_count()]
