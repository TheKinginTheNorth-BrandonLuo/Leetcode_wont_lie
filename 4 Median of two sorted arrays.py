#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:21:49 2020
#4. Median of two sorted arrays
@author: luofan
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1 + len2
        nums = [0] * length 
        i, j, f1, f2 = 0, 0, 0, 0
        if len1 == 0:
            nums = nums2
        elif len2 == 0:
            nums = nums1
        else:
            for index in range(length):
                if nums1[i] < nums2[j] and f1 == 0:
                    nums[index] = nums1[i]
                    if i != len1 - 1:
                        i += 1
                    else:
                        f1 = 1
                elif nums1[i] < nums2[j] and f1 == 1:
                    nums[index] = nums2[j]
                    if j != len2 - 1:
                        j += 1
                elif nums1[i] >= nums2[j] and f2 == 0:
                    nums[index] = nums2[j]
                    if j != len2 - 1:
                        j += 1
                    else:
                        f2 = 1
                else:
                    nums[index] = nums1[i]
                    if i != len1 - 1:
                        i += 1
        if length % 2 == 1:
            return nums[int(length / 2)]
        else:
            Median_index1 = int(length / 2 ) - 1 
            Median_index2 = int(length / 2)
            return float((nums[Median_index1] + nums[Median_index2]) / 2) 
obl = Solution()
test1 = [1,2]
test2 = [3,4]
print(obl.findMedianSortedArrays(test1,test2))                
                    