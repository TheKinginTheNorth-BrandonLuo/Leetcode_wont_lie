# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 20:40:58 2022

@author: Fan Luo
"""
"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is 
    less than 150 combinations for the given input.
    
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        
        def dfs(array, target, res, path):
            if target == 0:
                res.append(path)
                
            for i in range(len(array)):
                if array[i] > target:
                    break
                
                else:
                    dfs(array[i:], target - array[i], res, path + [array[i]])
                
        dfs(candidates, target, res, [])
        return res