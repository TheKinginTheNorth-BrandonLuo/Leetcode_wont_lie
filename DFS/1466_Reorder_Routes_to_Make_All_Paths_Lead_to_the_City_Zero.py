# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:51:25 2022

@author: Fan Luo
"""
"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
"""
import collections

class Solution:
    def minReorder(self, n, connections):
        graph = collections.defaultdict(list)
        
        for departure, destination in connections:
            graph[departure].append((destination, 1))
            graph[destination].append((departure, 0))
            
        visited = set()
        res = [0]
        
        def dfs(city, graph, visited, res):
            visited.add(city)
            
            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res[0] += cost
                    dfs(neighbor, graph, visited, res)
            
            
        dfs(0, graph, visited, res)
        return res[0]