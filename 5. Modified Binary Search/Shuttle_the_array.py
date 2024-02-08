class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10 #shift it to the left by 10
            nums[i] = nums[i] | nums[i + n] #store x, y in a single spot in binary
        j = 2 * n- 1 #storing nums toward the end of the array
        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1) #store the y value by bitwising it(&)
            x = nums[i] >> 10 #shifting the value to right by 10

            nums[j] =y
            nums[j - 1] = x
            j -= 2
        return nums