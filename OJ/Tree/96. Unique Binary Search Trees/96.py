class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        if n == 0:
        	return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
        	for j in range(i):
        		dp[i] += dp[j] * dp[i - 1 - j]
        return dp[-1]
        
s = Solution()
print s.numTrees(5)