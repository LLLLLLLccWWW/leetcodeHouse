class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        ans_id = logs[0][0]
        max_dur = logs[0][1]

        prev_time = logs[0][1]

        for i in range(1,len(logs)):
            emp_id,leave_time = logs[i]
            dur = leave_time - prev_time

            # 優先比較任務時長；若時長相同則取 ID 較小者
            if dur > max_dur or (dur == max_dur and emp_id < ans_id):
                max_dur = dur
                ans_id = emp_id

            prev_time = leave_time

        return ans_id

