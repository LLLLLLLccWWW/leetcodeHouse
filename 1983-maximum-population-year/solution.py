class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        pop = [0] * 101 # 記錄 1950 到 2050 年的人口變化

        # 標記出生與死亡帶來的變化量
        for birth,death in logs:
            pop[birth - 1950] += 1
            pop[death - 1950] -= 1

        max_pop = 0
        curr_pop = 0
        earliest_year = 1950

        # 計算前綴和獲得每年實際人口
        for year_offset in range(101):
            curr_pop += pop[year_offset]
            if curr_pop > max_pop:
                max_pop = curr_pop
                earliest_year = 1950 + year_offset

        return earliest_year
