# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:14:42 2022

@author: Fan Luo
"""
"""
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, 
    and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
    such as eval().
    
Input: s = "1 + 1"
Output: 2
"""
class Solution(object):
    def calculate(self, s):
        output = []
        sign = 1
        cur = 0
        stack = []
        
        for c in s:
            if c.isdigit():
               cur = cur * 10 + int(c)
               
            elif c in "+-":
                output += (cur * sign)
                cur = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1
                    
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 0
                
            elif c == ")":
                output += cur * sign
                output *= stack.pop()
                output += stack.pop()
                cur = 0
                
        return output + cur * sign
            