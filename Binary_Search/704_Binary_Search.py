# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:03:31 2022

@author: Fan Luo
"""
"""
704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    
if __name__ == '__main__':
    S = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(S.search(nums, target))