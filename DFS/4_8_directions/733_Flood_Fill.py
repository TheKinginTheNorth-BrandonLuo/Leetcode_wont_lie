# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:05:58 2022

@author: Fan Luo
"""
"""
733. Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
"""
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(r, c):
            image[r][c] = newColor
            for x, y in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= x < ROWS and 0 <= y < COLS and image[x][y] == original_color:
                    dfs(x, y)
            
        ROWS, COLS, original_color = len(image), len(image[0]), image[sr][sc]
        if original_color != newColor:
            dfs(sr, sc)
        
        return image