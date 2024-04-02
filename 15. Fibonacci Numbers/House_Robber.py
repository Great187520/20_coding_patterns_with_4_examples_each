class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        #[rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
#second solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for x in range(2, len(nums)):
            dp[x] = max(dp[x - 1], nums[x] + dp[x - 2])

        return dp[-1]