class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        n = len(nums)
        max = 0
        # populate initial state
        for i in range(n):
            heapq.heappush(pq, (nums[i][0], i, 0))
            nmax = max(nmax, nums[i][0])

        ans = [pq[0][0], nmax]

        while True:
            _, list_index, num_index = heapq.heappop(pq)

            # if current smallest number is the last item in its list, then break
            if num_index == len(nums[list_index]) - 1:
                break

            next_num = nums[list_index][num_index+1]
            nmax = max(nmax, next_num)
            heapq.heappush(pq, (next_num, list_index, num_index+1))

            if nmax - pq[0][0] < ans[1] - ans[0]:
                ans = [pq[0][0], nmax]

        return ans