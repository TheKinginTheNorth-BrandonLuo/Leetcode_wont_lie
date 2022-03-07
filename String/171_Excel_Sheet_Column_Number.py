# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 20:21:36 2022

@author: Fan Luo
"""
"""
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear in an Excel sheet, 
    return its corresponding column number.

Input: columnTitle = "A"
Output: 1

Input: columnTitle = "AB"
Output: 28
"""

class Solution:
    def titleToNumber(self, columnTitle):
        number = 0
        columnTitle = columnTitle.upper()
        
        for char in columnTitle:
            number = number *26
            number += ord(char) - ord("A") + 1
        
        return number