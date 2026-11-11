class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        # event1 開始時間 <= event2 結束時間，且 event2 開始時間 <= event1 結束時間
        return event1[0] <= event2[1] and event2[0] <= event1[1]
