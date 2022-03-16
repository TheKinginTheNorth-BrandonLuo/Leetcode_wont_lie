# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:31:41 2022

@author: Fan Luo
"""
"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
"""
from collections import Counter

class Solution:
    def minDominoRotations(self, tops, bottoms):
        if len(tops) != len(bottoms):
            return -1
        
        mutual_value_dic, count_tops, count_bottoms = Counter(), Counter(tops), Counter(bottoms)
        
        for i, j in zip(tops, bottoms):
            if i == j:
                mutual_value_dic[i] += 1
        
        for i in range(1, 7):
            if count_tops[i] + count_bottoms[i] - mutual_value_dic == len(tops):
                return min(count_tops[i], count_bottoms[i]) - mutual_value_dic[i]
        return -1