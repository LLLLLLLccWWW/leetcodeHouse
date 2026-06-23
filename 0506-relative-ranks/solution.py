class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # 步驟 1：建立一個與原本 score 同等長度的答案陣列
        n = len(score)
        answer = [''] * n

        # 步驟 2：將 (分數, 原始索引) 進行降序排序
        # enumerate(score) 會產生 (0, 分數), (1, 分數)... 
        # 我們以分數為基準 (x[1]) 由大到小排序
        sorted_scores = sorted(enumerate(score),key = lambda x: x[1],reverse = True)

        # 步驟 3：依據排序後的順序（即名次）指派獎牌
        for rank,(original_index, s) in enumerate(sorted_scores):
            if rank == 0:
                answer[original_index] = "Gold Medal"
            elif rank == 1:
                answer[original_index] = "Silver Medal"
            elif rank == 2:
                answer[original_index] = "Bronze Medal"
            else:
                # 程式的名次從 0 開始，所以實際名次要加 1，並轉成字串
                answer[original_index] = str(rank + 1)

        return answer
