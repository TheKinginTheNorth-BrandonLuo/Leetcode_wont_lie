# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 20:19:06 2022

@author: Fan Luo
"""
"""
282. Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

"""
class Solution:
    def addOperators(self, num, target):
        """
        5 - 3 + 4 + 5 * 2 * 3
        init sofar = 5
        - sofar += -3 -> 2
        + sofar +=  4 -> 6
        + sofar +=  5 -> 11
        * sofar  =  sofar - 5 + 5 * 2 -> 16  cand = 2  prev = 5  cand * prev = 10
        * sofar  =  sofar - 10 (which is prev(cand*prev)) + 10 * 3 = 36
        """
        N = len(num)
        output = []
        
        def dfs(i, sofar, res, prev):
            if i >= N:
                if res == target:
                    output.append("".join(sofar))
                    
            for j in range(i, N):
                cand = int(num[i:j + 1])
                if not sofar:
                    dfs(j + 1, sofar + [num[i:j + 1]], cand, cand)
                else:
                    dfs(j + 1, sofar + ["+"] + [num[i:j + 1]], res + cand, cand)
                    dfs(j + 1, sofar + ["-"] + [num[i:j + 1]], res - cand, -cand)
                    dfs(j + 1, sofar + ["*"] + [num[i:j + 1]], res - prev + cand * prev, cand * prev)
                    
                if num[i] == "0":
                    break
                    
        dfs(0, [], 0, None)
        return output