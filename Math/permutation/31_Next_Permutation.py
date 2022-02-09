# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 23:57:44 2022

@author: Fan Luo
"""
"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Input: nums = [1,2,3]
Output: [1,3,2]
"""
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # finding first decreasing numbers i
        
        # go back and find first number j just greater than i
        
        # swap i and j and sort numbers after j(original i)
        x,y = -1,-1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                x = i - 1
                break
                
        if x == -1:
            nums = nums.sort()
        else:
            for i in range(x + 1, len(nums)):
                if nums[x] < nums[i]:
                    y = i
                else:
                    break
            
            nums[x], nums[y] = nums[y], nums[x]
            nums[x + 1:] = sorted(nums[x + 1:])