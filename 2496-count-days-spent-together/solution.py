class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 輔助函式：將 "MM-DD" 轉換為一年中的第幾天 (1-indexed)
        def date_to_day_of_year(date_str:str)->int:
            month,day = map(int,date_str.split('-'))
            return sum(days_in_months[:month -  1]) + day

        start_a = date_to_day_of_year(arriveAlice)
        end_a = date_to_day_of_year(leaveAlice)
        start_b = date_to_day_of_year(arriveBob)
        end_b = date_to_day_of_year(leaveBob)

        # 共同重疊區間 [max(startA, startB), min(endA, endB)]
        latest_start = max(start_a,start_b)
        earliest_end = min(end_a,end_b)

        return max(0,earliest_end - latest_start + 1)
