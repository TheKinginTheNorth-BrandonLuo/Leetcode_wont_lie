# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:25:04 2022

@author: Fan Luo
"""
"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        
        ArithmeticError
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count:
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq:
                res.append(n)
                if len(res) == k:
                    return res