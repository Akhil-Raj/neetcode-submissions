class Solution:
    def maxSubArrayHelper(self, nums, i, j):
        if i == j:
            return nums[i]
        if i > j:
            return -20,000
        mid = (i + j) // 2
        maxLeftInd = mid
        maxRightInd = mid + 1
        sumLeft = nums[mid]
        sumRight = nums[mid + 1]
        maxSumLeft = sumLeft
        maxSumRight = sumRight

        for ind in range(mid - 1, i - 1, -1):
            sumLeft = sumLeft + nums[ind]
            if maxSumLeft < sumLeft:
                maxSumLeft = sumLeft
        
        for ind in range(mid + 2, j + 1):
            sumRight = sumRight + nums[ind]
            if maxSumRight < sumRight:
                maxSumRight = sumRight

        return max(self.maxSubArrayHelper(nums, i, mid), self.maxSubArrayHelper(nums, mid + 1, j), maxSumLeft + maxSumRight)


    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)