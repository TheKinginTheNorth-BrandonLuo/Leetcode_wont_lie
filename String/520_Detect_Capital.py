# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:13:19 2022

@author: Fan Luo
"""
"""
520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Input: word = "USA"
Output: true
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() == True:
            return True
        elif word.islower() == True:
            return True
        elif word[0].isupper() == True and word[1:].islower() == True:
            return True
        else:
            return False