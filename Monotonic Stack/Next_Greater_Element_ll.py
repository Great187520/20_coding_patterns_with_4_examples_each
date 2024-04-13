class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]

            stack.append(i)

        #handle the next greater element on the left side
            for i in range(n):
                if i == stack[-1]:
                    break
                while stack and nums[i] > nums[stack[-1]]:
                    ans[stack.pop()] = nums[i]

            return ans