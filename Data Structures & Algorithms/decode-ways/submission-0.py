class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s))]
        dp[0] = 1 if s[0] != '0' else 0
        if len(s) == 1:
            return dp[0]
        for i in range(1, len(s)):
            # When last letter alone is considered
            if s[i] != '0':
                dp[i] += dp[i - 1]
            # when last and second-last is considered together
            if (s[i - 1] == '1') or (s[i - 1 : i + 1] in ['20', '21', '22', '23', '24', '25', '26']):
                dp[i] = dp[i] + (dp[i - 2] if i > 1 else 1)

        return dp[-1]