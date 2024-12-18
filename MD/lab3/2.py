from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = {}

        for i in range(n):
            prices[i] = float('inf')
        prices[src] = 0.0


        for _ in range(k + 1):
            temp = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if p + prices[s] < temp[d]:
                    temp[d] = p + prices[s]

            prices = temp

        return -1 if prices[dst] == float("inf") else int(prices[dst])

solution = Solution()
print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
