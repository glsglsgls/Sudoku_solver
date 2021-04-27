import sudoku
import numpy as np

b = sudoku.sudoku()
b.createboard()
#b.checkPossibility()
#print(b.board)

#input = np.array([[1,5,6,4,0,3,7,0,8],[7,0,9,0,1,8,3,0,6],[4,8,3,7,9,6,1,2,5]])
#b.readboard(input)
#for k in range(1,3):    
#    for i in range(0,3):
#        for j in range(0,9):
#            print(b.board[i,j])
#            if b.board[i,j] == 0:
#                list = b.collect_possible_numbers(i,j)
#                print(list)
#                if len(list) == 1:
#                    b.board[i,j] = list.pop()
#                else:
#                    b.board[i,j] = 0 #b.collect_possible_numbers(i,j)
#    print("new iteration")
#print(b.board)
             
