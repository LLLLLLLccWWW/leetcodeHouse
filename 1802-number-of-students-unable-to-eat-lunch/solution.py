class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = [students.count(0),students.count(1)]

        for sandwich in sandwiches:
            # 若沒有學生喜歡當前頂端的三明治，流程結束
            if count[sandwich] == 0:
                return count[0] + count[1]
            count[sandwich] -= 1

        return 0
