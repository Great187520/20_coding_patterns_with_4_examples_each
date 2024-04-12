class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, n):
            # base case
            if i == len(nums):
                return 1 if n == 0 else 0
            return dp(i + 1, n + nums[i]) + dp(i + 1, n - nums[i])
        return dp(0, target)