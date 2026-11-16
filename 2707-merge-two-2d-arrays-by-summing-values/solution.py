class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i,j = 0,0
        n,m = len(nums1),len(nums2)

        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                ans.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                ans.append([id1, val1])
                i += 1
            else:
                ans.append([id2,val2])
                j += 1

        # 將尚未走訪完的剩餘區段直接併入結果
        if i < n:
            ans.extend(nums1[i:])
        if j < m:
            ans.extend(nums2[j:])

        return ans
