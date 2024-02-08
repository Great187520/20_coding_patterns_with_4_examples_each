class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts,ends,output = [],[],[]

        for i, (start, end) in enumerate(intervals):
            heapq.heappush(starts,(start, i))
            heapq.heappush(ends, (end,i))
        heapq.heappush((start,float('inf'), -1))
        start = float('-inf')
        while ends:
            end, i_end = heapq.heappop(ends)
            while starts and start < end:
                start, i_start = heapq.heappop(starts)
                if start >= end: break
            output.append ((i_end, i_start))

        return [i2 for i1, i2  in sorted(output)]
    