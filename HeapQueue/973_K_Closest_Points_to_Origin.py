# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:59:49 2022

@author: Fan Luo
"""
"""
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""
import heapq

class Solution:
    def kClosest(self, points, k):
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
            
        # sort heap
        heapq.heapify(minHeap)
        
        res = []
        while k > 0:
            dist, x , y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res