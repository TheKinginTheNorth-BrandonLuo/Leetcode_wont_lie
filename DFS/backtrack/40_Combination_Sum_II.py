# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 20:14:04 2022

@author: Fan Luo
"""
"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

"""
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack(array, target, res, path):
            if target == 0:
                res.append(path)
            if target < 0:
                return 
            for i in range(len(array)):
                if i > 0 and array[i] == array[i - 1]:
                    continue
                else:
                    backtrack(array[i + 1:], target - array[i], res, path + [array[i]])
                
        backtrack(candidates, target, res, [])
        return res