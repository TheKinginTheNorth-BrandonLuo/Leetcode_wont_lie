# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:13:05 2022

@author: Fan Luo
"""
"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        n = 0
        while nums != []:
            root = nums.pop()
            n += 1
            
            if n == k:
                return root