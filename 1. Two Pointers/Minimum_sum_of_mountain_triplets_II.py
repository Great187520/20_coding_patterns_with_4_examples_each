class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if len(nums) < 3: return -1

        # find the prefix
        min_num = math.inf
        prefix = [math.inf] * len(nums)
        for i, n in enumerate(nums):
            prefix[i] = min_num = min(min_num, n)

        # find the suffix
        suffix = [math.inf] * len(nums)
        for i, n in enumerate(nums[::-1]):
            suffix[len(nums) - i - 1] = min_num = min(min_num, n)

        # find triplets
        min_sum = math.inf
        for i in range(1, len(nums) - 1):
            min_left = prefix[i - 1]
            min_right = suffix[i + 1]

            # triplet is valid!
            if min_left < nums[i] > min_right:
                min_sum = min(min_sum, min_left + nums[i] + min_right)

        return -1 if min_sum == math.inf else min_sum