# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 21:10:28 2022

@author:Fan Luo
"""
"""
941. Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
            arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            arr[i] > arr[i + 1] > ... > arr[arr.length - 1
                                                                      
Input: arr = [0,3,2,1]
Output: true
"""
class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        
        left, right = 0, len(arr) - 1
        
        while left < len(arr - 1) and arr[left] < arr[left + 1]:
            left += 1
            
        while right >= 0 and arr[right] > arr[right - 1]:
            right -= 1
            
        return right == left and left != 0 and right != len(arr) - 1