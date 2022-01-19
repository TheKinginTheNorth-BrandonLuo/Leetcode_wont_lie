# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:51:43 2022

@author: Fan Luo
"""
"""
96. Unique Binary Search Trees
Given an integer n, return the number of structurally unique BST's (binary search trees)
 which has exactly n nodes of unique values from 1 to n.
 
Input: n = 3
Output: 5
"""
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def numTrees(self, n):
        dp = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += dp[j] * dp[i - j - 1]
            dp.append(count)
        return dp.pop()
    
if __name__ == '__main__':
    None


















































   