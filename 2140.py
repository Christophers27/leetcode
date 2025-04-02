class Solution(object):
    def mostPoints(self, questions):
        N = len(questions)
        dp = [0] * N

        dp[-1] = questions[-1][0]

        for i in range(N - 1)[::-1]:
            nextAnsIdx = i + questions[i][1] + 1
            dp[i] = max(
                questions[i][0] + (dp[nextAnsIdx] if nextAnsIdx < N else 0), dp[i + 1]
            )

        return dp[0]
