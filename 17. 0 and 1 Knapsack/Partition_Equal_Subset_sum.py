class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot/2 != tot//2: return False

        @cache
        def dp(i, amt):
            #base case
            if i >= len(nums) or amt >= tot/2:
                return amt == tot/2
            
            return dp(i + 1, amt + nums[i]) or dp(i + 1, amt)
        return dp(0, 0)
    
#second solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                #if (t + nums[i]) == target:
                    #return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False