class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        # 1. 將兩個陣列分別進行遞增排序
        seats.sort()
        students.sort()

        # 2. 計算對應位置的絕對差值並加總
        return sum(abs(seat - student) for seat,student in zip(seats,students))
