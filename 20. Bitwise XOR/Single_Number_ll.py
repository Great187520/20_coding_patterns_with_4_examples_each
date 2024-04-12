class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for x in nums:
            two = two ^ (one & x)
            one = one ^ x
            not_three = ~(two & one)

            one,two = not_three & one, not_three & two

        return one