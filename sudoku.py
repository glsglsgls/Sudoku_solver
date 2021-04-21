import numpy as np
class sudoku:

    def __init__(self):
        self.board = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
        self.startList = [1,2,3,4,5,6,7,8,9]

    def readboard(self, board_input):
        self.board = board_input
    
    def collect_possible_numbers(self, i, j):
        collected_list = self.startList.copy()
        for x in range(0,9):
            if collected_list.__contains__(self.board[i,x]):
                collected_list.remove(self.board[i,x])
        for y in range(0,3):
            if collected_list.__contains__(self.board[y,j]):
                collected_list.remove(self.board[y,j])
        for x in range(j//3*3,j//3*3+3):
            for y in range(0,3):
                if collected_list.__contains__(self.board[y,x]):
                    collected_list.remove(self.board[y,x])
        return collected_list
       
    

        
        


