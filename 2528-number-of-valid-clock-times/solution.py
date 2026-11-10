class Solution:
    def countTime(self, time: str) -> int:
        hours_choices = 1
        minutes_choices = 1

        # 1. 討論小時部分 (time[0], time[1])
        h1,h2 = time[0],time[1]
        if h1 == '?' and h2 == '?':
            hours_choices = 24
        elif h1 == '?':
            hours_choices = 3 if h2 <= '3' else 2
        elif h2 == '?':
            hours_choices = 4 if h1 == '2' else 10

        # 2. 討論分鐘部分 (time[3], time[4])
        m1,m2 = time[3],time[4]
        if m1 == '?':
            minutes_choices *= 6
        if m2 == '?':
            minutes_choices *= 10

        return hours_choices * minutes_choices

