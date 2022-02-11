# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:23:11 2022

@author: Fan Luo
"""
"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
"""
class Solution:
    def isAlienSorted(self, words, order):
        dic = {c:i for i, c in enumerate(order)}
        res = []
        
        for w in words:
            tmp = []
            for c in w:
                tmp.append(dic[c])
            res.append(tmp)
            
        for i in range(1, len(res)):
            if res[i - 1] > res[i]:
                return False
            
        return True
    
if __name__ == '__main__':
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, order))