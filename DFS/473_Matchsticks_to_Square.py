# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:03:34 2022

@author: Fan Luo
"""
"""
473. Matchsticks to Square

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
"""
class Solution:
    def makesquare(self, matchsticks):
        edge_length = sum(matchsticks) // 4
        if sum(matchsticks) / 4 != edge_length:
            return False
        sides = [0] * 4
        matchsticks.sort(reverse = True)
        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= edge_length:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    # if not true, we need to remove
                    sides[j] -= matchsticks[i]
            return False
        
        return dfs(0)
        