# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:23:43 2022

@author: Fan Luo
"""
"""
71. Simplify Path

Given a string path, which is an absolute path (starting with a slash '/') to a file 
    or directory in a Unix-style file system, convert it to the simplified canonical path.
    
In a Unix-style file system, a period '.' refers to the current directory, 
    a double period '..' refers to the directory up a level, 
    and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, 
    any other format of periods such as '...' are treated as file/directory names.
    
The canonical path should have the following format:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
"""
class Solution(object):
    def simplifyPath(self, path):
        stack = []
        path = path.split('/')
        
        for root in path:
            if not root or root == '.':
                continue
            if root == '..':
                if stack:
                    stack.pop()
            
            else:
                stack.append(root)
        return '/' + '/'.join(stack)
    
if __name__ == '__main__':
    path = "/home/foo/../"
    print(Solution().simplifyPath(path))