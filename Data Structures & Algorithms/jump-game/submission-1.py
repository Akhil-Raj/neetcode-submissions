class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        totMax = nums[0]
        for ind in range(1, len(nums)):
            if ind > totMax:
                return False
            currMax = ind + nums[ind]
            if currMax >= len(nums) - 1:
                return True
            if currMax > totMax:
                totMax = currMax
        return False