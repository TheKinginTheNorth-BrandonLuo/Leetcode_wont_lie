# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:30:28 2022

@author: Fan Luo
"""
"""
151. Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Input: s = "the sky is blue"
Output: "blue is sky the"
"""
class Solution(object):
    def reverseWords(self, s):
        res = s.split()[::-1]
        q = res[0]
        for i in range(1, len(res)):
            q = q + " " + res[i]
        return q
    
if __name__ == '__main__':
    s = "the sky is blue"
    print(Solution().reverseWords(s))