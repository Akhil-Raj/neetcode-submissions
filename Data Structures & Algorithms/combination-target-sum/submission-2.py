class Solution:
    combs = []
    def helper(self, nums, target, ind, output):
        if target == 0:
            self.combs.append([ele for ele in output])
            return
        if ind >= len(nums) or target < 0 :
            return
        
        # skip ele
        self.helper(nums, target, ind + 1, output.copy())
        # take ele
        output.append(nums[ind])
        self.helper(nums, target - nums[ind], ind, output.copy())

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.combs = []
        self.helper(nums, target, 0, [])
        return self.combs