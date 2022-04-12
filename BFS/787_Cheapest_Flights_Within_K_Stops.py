# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:46:21 2022

@author: Fan Luo
"""
"""
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
"""
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k + 1):
            tmp_prices = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p
            prices = tmp_prices
            
        return -1 if prices[dst] == float("inf") else prices[dst]