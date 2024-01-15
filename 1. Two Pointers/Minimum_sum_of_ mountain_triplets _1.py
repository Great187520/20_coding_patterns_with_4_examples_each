class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if len(nums) < 3: return - 1

        min_sum = math.inf
        for i in range(1, len(nums) - 1):
            min_left = min(nums[:1])
            min_right = min(nums[i+1:])

            # check if this mountain is valid
            if min_left < nums[i] > min_right:
                min_sum = min(min_sum, min_left + nums[i] + min_right)

        return -1 if min-sum ==  math.inf else min_sum