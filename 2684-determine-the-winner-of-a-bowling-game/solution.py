class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calc_score(pins: list[int]) -> int:
            score = 0
            double_turns = 0
            for x in pins:
                if double_turns > 0:
                    score += x << 1
                    double_turns -= 1
                else:
                    score += x

                if x == 10:
                    double_turns = 2

            return score

        s1,s2 = calc_score(player1),calc_score(player2)
        if s1 > s2:
            return 1
        if s2 > s1:
            return 2
        return 0
