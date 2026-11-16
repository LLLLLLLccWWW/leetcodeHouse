class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        return [int(ch) for num in nums for ch in str(num)]
