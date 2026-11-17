class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds,rem = divmod(time, n - 1)
        if rounds % 2 == 0:
            return 1 + rem
        return n - rem
