# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:27:45 2022

@author: jiarong xia
"""
"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""
class Solution:
    def partition(self, s):
        res = []
        path = []
        def dfs(i):
            if i >= len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    path.append(s[i:j + 1])
                    dfs(j + 1)
                    """
                    start next search
                    """
                    path.pop()
            
        dfs(0)
        return res
    
if __name__ == '__main__':
    print(Solution().partition("aab"))
            