# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:17:48 2022

@author: Fan Luo
"""
"""
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
"""
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, k):
        g = collections.defaultdict(list)
        visited = set()
        queue = collections.deque()
        res = []
        
        self.convert_to_graph(root, None, g)
        
        queue.append((target, 0))
        
        while queue:
            node, distance = queue.popleft()
            visited.add(node)
            if distance == k:
                res.append(node.val)
            for nei in g[node]:
                if nei not in visited:
                    queue.append((nei, distance + 1))
                    
        return res
        
    def convert_to_graph(self, node, parent, g):
        if not node:
            return
        
        if parent:
            g[node].append(parent)
            
        if node.right:
            g[node].append(node.right)
            self.convert_to_graph(node.right, node, g)
        
        if node.left:
            g[node].append(node.left)
            self.convert_to_graph(node.left, node, g)