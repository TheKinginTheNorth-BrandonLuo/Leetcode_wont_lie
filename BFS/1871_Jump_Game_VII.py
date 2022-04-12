# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:24:37 2022

@author: Fan Luo
"""
"""
1871. Jump Game VII

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

    i + minJump <= j <= min(i + maxJump, s.length - 1), and
    s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
"""
from collections import deque

class Solution:
    def canReach(self, s, minJump, maxJump):
        queue, farthest = deque([0]), 0
        
        while queue:
            i = queue.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    queue.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump
        return False