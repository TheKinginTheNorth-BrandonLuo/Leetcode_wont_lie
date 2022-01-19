# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:33:22 2022

@author: Fan Luo
"""
"""
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence
 of bits so that it can be stored in a file or memory buffer, 
 or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
 There is no restriction on how your serialization/deserialization algorithm should work. 
 You just need to ensure that a binary tree can be serialized to a string and 
 this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append("Null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        self.i = 0
        
        def dfs():
            if nodes == "Null":
                self.i += 1
                return (None)
            
            node = TreeNode(int(node[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            
            return node
        return dfs















































































































"""

