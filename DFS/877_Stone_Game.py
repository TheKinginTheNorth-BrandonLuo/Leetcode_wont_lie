# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:04:40 2022

@author: Fan Luo
"""
"""
877. Stone Game

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
"""
from functools import lru_cache

class Solution:
    def stoneGame(self, piles):
        N = len(piles)
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j: # no more stones left
                return 0
            # decide player turn
            if (j - i) % 2 != 0: # alex turn
                return max(piles[i] + dfs(i + 1, j), piles[j] + dfs(i, j - 1))
            else: # bob turn and he trys to minimize alex result
                return min(-piles[i] + dfs(i + 1, j), -piles[j] + dfs(i, j - 1))
            
        return dfs(0, N - 1) > 0