import numpy as np
import random
import tkinter
from window import getboard

class sudoku:

    def __init__(self):
        self.board = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
        self.startList = [1,2,3,4,5,6,7,8,9]

    def readboard(self, board_input):
        self.board = board_input

    def createboard(self):
        for i in range(0,9,3):
            for j in range(0,9,3):
                list = [1,2,3,4,5,6,7,8,9]
                random.shuffle(list)
                for y in range(j,j+3):
                    for x in range(i,i+3):
                        possible_list = self.collect_possible_numbers(x,y)
                        count = 1
                        while count < 10:
                            if possible_list.__contains__(list[-1]):
                                self.board[x, y] = list.pop()
                                #print("new row")
                                #print(self.board)
                                break
                            else:
                                #print("new row")
                                #print(self.board)
                                self.movelist(list)
                            count += 1
        getboard(self.board)
    
    def movelist(self, list):
        list.append(list.pop(list.index(list[0])))
        return list
    
    def checkPossibility(self):
        for i in range(0,3):
            for j in range(0,9):
                count = 1
                while True:
                    list = self.collect_possible_numbers(i,j)
                    if len(list) == 1:
                        break
                    self.board[i,j] = random.choice(list)
                    count +=1
                    if count == 1000:
                        print("to many iterations; row: " + str(i) + "column: " + str(j))
                        break


    def collect_possible_numbers(self, i, j):
        collected_list = self.startList.copy()
        for x in range(0,9):
            if collected_list.__contains__(self.board[i,x]):
                collected_list.remove(self.board[i,x])
        for y in range(0,3):
            if collected_list.__contains__(self.board[y,j]):
                collected_list.remove(self.board[y,j])
        for x in range(j//3*3,j//3*3+2):
            for y in range(0,3):
                if collected_list.__contains__(self.board[y,x]):
                    collected_list.remove(self.board[y,x])
        return collected_list
       
    

        
        


