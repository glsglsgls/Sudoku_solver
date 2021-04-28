import sudoku
import numpy as np
import window

b = sudoku.sudoku()
b.createboard()
#b.transposetable()

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
 
#my = Canvas()
#my.create_line(0, 25, 400, 25)
#my.place(x=0, y=87)
#my1 = Canvas()
#my1.create_line(0, 25, 400, 25)
#my1.place(x=0, y=196)   

#my2 = Canvas()
#my2.create_line(25, 0, 25, 1500)
#my2.place(x=82, y=0)
#my3 = Canvas()
#y3.create_line(25, 0, 25, 1500)
#my3.place(x=191, y=0)"""
             