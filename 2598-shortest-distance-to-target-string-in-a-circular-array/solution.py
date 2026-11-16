class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)

        for step in range(n // 2 + 1):
            right = (startIndex + step) % n
            left = (startIndex - step + n) % n

            if words[right] == target or words[left] == target:
                return step

        return -1
