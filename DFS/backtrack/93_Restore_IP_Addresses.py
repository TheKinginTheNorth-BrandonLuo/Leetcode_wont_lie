# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:27:58 2022

@author: Fan Luo
"""
"""
93. Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
"""

class Solution:
    def restoreIpAddresses(self, s):
        res = []
        if len(s) > 12 or len(s) < 4:
            return res
        
        def dfs(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) <= 255 and (i == j or s[i] != '0'):
                    dfs(j + 1, dots + 1, curIP + s[i:j+1] + ".")
        
        dfs(0, 0, "")
        return res