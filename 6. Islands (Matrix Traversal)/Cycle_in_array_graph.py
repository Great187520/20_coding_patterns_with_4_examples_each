class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        checked = set() #set has constant time O(1)
        for i in range(n):
            if i not in checked:
                cycle_set = set()
                while True:
                    if i in cycle_set:
                        return True
                    checked.add(i)
                    cycle_set.add(i)
                    prev, i = i, (i+nums[i])%n #nums of jumps
                    
                    if prev == 1:
                        # unicycle check
                        break
                    if nums[prev]>0 != nums[i]<0: #check weather the signs are the same
                        break
        return False