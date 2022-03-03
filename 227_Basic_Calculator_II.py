# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:48:46 2022

@author: Fan Luo
"""
"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval()

Input: s = " 3/2 "
Output: 1

Input: s = " 3+5 / 2 "
Output: 5
"""
class Solution(object):
    def calculate(self, s):
        stack = []
        cur = 0
        sign = '+'
        
        for c in s + "+":
            if c.isdigit():
                cur = 10 * cur + int(c)
            elif c in "+-*/":
                if sign == "+":
                    stack.append(cur)
                elif sign == "-":
                    stack.append(-cur)
                elif sign == "*":
                    stack.append(stack.pop() * cur)
                elif sign == "/":
                    stack.append(int(stack.pop() / cur))
                cur = 0
                sign = c
        return sum(stack)