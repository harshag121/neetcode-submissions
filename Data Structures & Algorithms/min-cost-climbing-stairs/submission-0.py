class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _  in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for _ in range(2,len(cost)):
            dp[_] = cost[_] + min(dp[_-1],dp[_-2])
        
        return min(dp[-1], dp[-2])

        
        