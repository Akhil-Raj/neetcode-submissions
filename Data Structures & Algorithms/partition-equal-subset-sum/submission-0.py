class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        # dp[i][j] = Can we form sum 'j' using elements till index 'i'? To find : dp[n - 1][s // 2]
        dp = [[0 for i in range(s // 2 + 1)] for j in range(len(nums))]

        for i in range(len(dp[0])):
            dp[0][i] = 1 if (i == nums[0]) else 0
        
        for ind in range(1, len(nums)):
            for su in range(len(dp[0])):
                dp[ind][su] = dp[ind - 1][su] or (dp[ind - 1][su - nums[ind]] if (su >= nums[ind]) else 0)
        
        return bool(dp[-1][-1])
