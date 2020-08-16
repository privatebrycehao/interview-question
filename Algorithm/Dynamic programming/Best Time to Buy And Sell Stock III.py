# link ===> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# dp, 从左到右，找最大的收益，在从右到左找最大收益
# 中间找隔板
# Sample: [3,3,5,0,0,3,1,4]
# 从左到右的最大收益是 第五天买入0， 第六天卖出 3， profit 3 
# 从右到左的最大收益是，第七天买入1，第八天卖出4， profit 3
# 收益是 3+3 6
# P1是从左到右从第0天到第i天的最大收益，
# p1 = [0,0,2,2,2,3,3,4]
# p2 = [4,4,4,4,4,3,3,0]
# P1,P2交叉和最大为6
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        p1 = [0] * n
        p2 = [0] * n
        minV = prices[0]
        for i in range(1,n):
            minV = min(minV, prices[i])
            p1[i] = max(p1[i-1], prices[i]-minV)
        maxV = prices[-1]
        for i in range(n-2, -1, -1):
            maxV= max(maxV, prices[i])
            p2[i] = max(p2[i+1], maxV - prices[i])
        ans = 0
        for i in range(n):
            ans = max(ans, p1[i] + p2[i])
        return ans 