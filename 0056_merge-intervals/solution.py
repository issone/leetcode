from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = []
        intervals.sort(key=lambda x: x[0])  # 先按左区间端点进行排序
        for interval in intervals:

            if not new_intervals or new_intervals[-1][1] < interval[0]:  # 上一个区间的右端点比当前区间的左端点还小，不能合并，直接插入
                new_intervals.append(interval)
            else:  # 当前区间左端点，一定比上一个区间的左端点大，当前区间左端点小于上一个区间的右端点时，一定重叠，合并后的新的区间右端点，是两个区间中右端点最大的那个
                new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
        return new_intervals
