# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:36:35 2022

@author: Fan Luo
"""
"""
1958. Check if Move is Legal

You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:
    
Given two integers rMove and cMove and a character color representing the color you are playing as (white or black), return true if changing cell (rMove, cMove) to color color is a legal move, or false if it is not legal.

Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
Output: true
Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
"""
class Solution:
    def checkMove(self, board, rMove, cMove, color):
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        board[rMove][cMove] = color
        
        def legal(row, col, color, direc):
            dr, dc = direc
            row, col = row + dr, col + dc
            length = 1
            
            while 0 <= row < ROWS and 0 <= col < COLS:
                length += 1
                if board[row][col] == ".":
                    return False
                if board[row][col] == color:
                    return length >= 3
                row, col = row + dr, col + dc
            return False
        
        for d in directions:
            if legal(rMove, cMove, color, d):
                return True
        return False