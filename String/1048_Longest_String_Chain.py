# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:11:36 2022

@author: Fan Luo
"""
"""
1048. Longest String Chain

You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
"""

class Solution:
    def longestStrChain(self, words):
        words.sort(key = lambda word: len(word))
        
        dic = {}
        res = 0
        
        for word in words:
            count = 1
            for i in range(len(word)):
                tmp = word[:i] + word[i + 1:]
                if tmp in dic:
                    count = max(count, dic[tmp] + 1)
            dic[word] = count
            res = max(res, dic[word])
            
        return res