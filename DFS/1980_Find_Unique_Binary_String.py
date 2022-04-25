# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:43:16 2022

@author: Fan Luo
"""
"""
1980. Find Unique Binary String

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
"""
class Solution:
    def findDifferentBinaryString(self, nums):
        self.res, n = "", len(nums[0])
        
        def dfs(cur):
            if self.res:
                return
            
            if len(cur) == n:
                if cur not in nums:
                    self.res = cur
                return
            
            for i in range(2):
                dfs(cur + str(i))
                
        dfs("")
        return self.res