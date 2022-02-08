# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:15:28 2022

@author: Fan Luo
"""
"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        res = []
        self.backtrack(range(1, n + 1), k, res, [])
        return res
        
        
    def backtrack(self, array, k, res, path):
        if len(array) < k:
            return
        
        if k == 0:
            res.append(path)
            
        else:
            for i in range(len(array)):
                self.backtrack(array[i + 1:], k - 1, res, path + [array[i]])
                
if __name__ == '__main__':
    print(Solution().combine(4, 2))