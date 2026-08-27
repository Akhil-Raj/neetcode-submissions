class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -20000
        subMaxSum = 0
        for num in nums:
            subMaxSum += num
            if subMaxSum > maxSum:
                maxSum = subMaxSum
            if subMaxSum < 0:
                subMaxSum = 0
        return maxSum