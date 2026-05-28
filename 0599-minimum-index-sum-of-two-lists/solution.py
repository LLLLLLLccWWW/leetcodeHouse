class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index1 = {v:i for i,v in enumerate(list1)}

        min_sum = float('inf')
        result = []

        for j, restaurant in enumerate(list2):
            if restaurant in index1:
                total = index1[restaurant] + j  # index sum

                if total < min_sum:
                    min_sum = total
                    result = [restaurant]   # 更新結果
                elif total == min_sum:
                    result.append(restaurant)   # 相同最小值，加入
        
        return result

