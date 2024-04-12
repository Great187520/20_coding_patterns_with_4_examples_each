class Solution:
    def longestPalindromeSubseg(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])
    
    def longestCommobSubsequence(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        dp = [[0] * (M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[N][M]
    
# dynamic programming
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [ [0] * (len(s) + 1) for i in range(len(s) + 1)]
        res = 0

        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                res = max(res, dp[i][j])
        return res