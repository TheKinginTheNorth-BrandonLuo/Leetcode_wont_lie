# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:55:24 2022

@author: Fan Luo
"""
"""
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
    and the combinations may be returned in any order.
    
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
"""
class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        self.dfs(1, k, n, res, [])
        return res
        
    def dfs(self, start, k, n, res, path):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
            return
        for i in range(start, 10):
            self.dfs(i + 1, k - 1, n - i, res, path + [i])
            
if __name__ == '__main__':
    print(Solution().combinationSum3(3, 9))
