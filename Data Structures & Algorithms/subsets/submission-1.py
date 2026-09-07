class Solution:
    subsets_total = []

    def subsets_help(self, output, nums, ind):
        if ind >= len(nums):
            self.subsets_total.append([ele for ele in output if ele != -100])
            return
        # ele not taken
        output[ind] = -100
        self.subsets_help(output, nums, ind + 1)
        # ele taken
        output[ind] = nums[ind]
        self.subsets_help(output, nums, ind + 1)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets_total = []
        output = [-100 for i in range(len(nums))]
        self.subsets_help(output, nums, 0)
        return self.subsets_total