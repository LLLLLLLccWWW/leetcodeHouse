class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # 依據每箱的單元數 (x[1]) 由大到小排序
        boxTypes.sort(key=lambda x:x[1],reverse=True)

        total_units = 0

        for num_boxes,units_per_box in boxTypes:
            if truckSize <=  0:
                break

            # 實際可裝入的箱子數量為 min(該種類箱子總數, 卡車剩餘容量)
            take_boxes = min(num_boxes,truckSize)
            total_units += take_boxes * units_per_box
            truckSize -= take_boxes

        return total_units
