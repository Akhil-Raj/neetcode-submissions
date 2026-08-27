class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = True
        for ind in range(len(nums) - 2, -1, -1):
            for ind2 in range(ind + 1, min(ind + nums[ind] + 1, len(nums))):
                if nums[ind2] is True:
                    nums[ind] = True
        
        return nums[0] is True