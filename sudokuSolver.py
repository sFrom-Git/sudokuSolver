from SudokuBoard import *
import random

newBoard = SudokuBoard()

gameOver = False
while gameOver == False:

	b = newBoard.returnValue()

	print()
	print(" _____________________________")
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 1".format(b[0][0],b[0][1],b[0][2],b[0][3],b[0][4],b[0][5],b[0][6],b[0][7],b[0][8]))
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 2".format(b[1][0],b[1][1],b[1][2],b[1][3],b[1][4],b[1][5],b[1][6],b[1][7],b[1][8]))
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 3".format(b[2][0],b[2][1],b[2][2],b[2][3],b[2][4],b[2][5],b[2][6],b[2][7],b[2][8]))
	print("|-----------------------------|")
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 4".format(b[3][0],b[3][1],b[3][2],b[3][3],b[3][4],b[3][5],b[3][6],b[3][7],b[3][8]))
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 5".format(b[4][0],b[4][1],b[4][2],b[4][3],b[4][4],b[4][5],b[4][6],b[4][7],b[4][8]))
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 6".format(b[5][0],b[5][1],b[5][2],b[5][3],b[5][4],b[5][5],b[5][6],b[5][7],b[5][8]))
	print("|-----------------------------|")
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 7".format(b[6][0],b[6][1],b[6][2],b[6][3],b[6][4],b[6][5],b[6][6],b[6][7],b[6][8]))
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 8".format(b[7][0],b[7][1],b[7][2],b[7][3],b[7][4],b[7][5],b[7][6],b[7][7],b[7][8]))
	print("| {}  {}  {} | {}  {}  {} | {}  {}  {} | 9".format(b[8][0],b[8][1],b[8][2],b[8][3],b[8][4],b[8][5],b[8][6],b[8][7],b[8][8]))
	print(" =============================")
	print("  a  b  c   d  e  f   g  h  i")
	print()

	#userInput = input("??? ").split()
	#x, y = (ord(userInput[0][0]) - 97), (int(userInput[0][1]) - 1)
	#i = int(userInput[-1])

	
	x = random.randint(0, 8)
	y = random.randint(0, 8)
	i = random.randint(1, 9)
	

	if newBoard.insertValue((x, y), i) == True:
		pass
	else:
		print("\nInvalid placement.")