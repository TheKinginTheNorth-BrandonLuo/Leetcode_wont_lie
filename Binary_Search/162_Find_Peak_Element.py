# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:35:16 2022

@author: Fan Luo
"""
"""
162. Find Peak Element
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""
class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2 # note (4+5) // 2 == 4 not 5
            
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
                
        return left
