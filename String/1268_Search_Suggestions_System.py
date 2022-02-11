# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:08:16 2022

@author: Fan Luo
"""
"""
1268. Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
"""
class Solution:
    def suggestedProducts(self, products, searchWord):
        res = []
        products.sort()
        
        for i, c in enumerate(searchWord):
            tmp = []
            for p in products:
                if i < len(p) and c == p[i]:
                    tmp.append(p)
            res.append(tmp[:3])
            products = tmp
            
        return res
        