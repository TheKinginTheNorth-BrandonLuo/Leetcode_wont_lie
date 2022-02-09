# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 23:01:54 2022

@author: Fan Luo
"""
"""
60. Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Input: n = 4, k = 9
Output: "2314"
"""
import math

class Solution(object):
    def getPermutation(self, n, k):
        res = []
        index = k - 1
        nums = [str(i) for i in range(1, n + 1)]
        factorial = math.factorial(n)
        
        while nums:
            factorial = factorial // len(nums)
            pos = index // factorial
            number = nums.pop(pos)
            res.append(number)
            index = index % factorial
            
        return "".join(res)
    
class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        res = []
        self.dfs(res, [], nums)
        return res[k - 1]
    
    
    def dfs(self, res, stack, nums):
        if len(nums) == 0:
            res.append("".join(stack))
            
        for i in range(len(nums)):
            stack.append(nums[i])
            self.dfs(res, stack, nums[:i] + nums[i + 1:])
            stack.pop()
    
    
if __name__ == '__main__':
    print(Solution().getPermutation(4, 9))