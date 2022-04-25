# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:39:40 2022

@author: Fan Luo
"""
"""
332. Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
"""
import collections

class Solution:
    def findItinerary(self, tickets):
        target = collections.defaultdict(list)
        tickets.sort(key = lambda x: x[1], reverse=True)
        for departure, destination in tickets:
            target[departure].append(destination)
        
        
        res = []
        
        def dfs(departure):
            destination = target[departure]
            while destination:
                dfs(destination.pop())
            res.append(departure)
          
        dfs("JFK")
        return res[::-1]
            
        