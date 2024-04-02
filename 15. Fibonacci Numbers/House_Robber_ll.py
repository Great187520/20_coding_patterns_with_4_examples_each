class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 3:
            return max(nums)
        
        def helper(dp):
            dp[1] = max(dp[0], dp[1])

            for x in range(2, len(dp)):
                dp[x] = max(dp[x - 1], dp[x] + dp[x - 2])

            return dp[-1]
        
        p1 = helper(nums[:len(nums) - 1])
        p2 = helper(nums[1:])
        return max(p1, p2)


        #second solution
    class Solution:
        def rob(self, nums: List[int]) -> int:
            if not nums: return 0
            if len(nums) == 1: return nums[0]

            dp1, dp2 = 0,0
            for n in nums[:-1]:
                tmp = dp1
                dp1 = max(dp2+n, dp1)
                dp2 = tmp 

            dpp1, dpp2 = 0,0
            for n in nums[1:]:
                tmp = dpp1
                dpp1 = max(dpp2+n, dpp1)
                dpp2 = tmp 

            return max(dp1,dpp1)