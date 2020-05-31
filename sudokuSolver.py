from SudokuBoard import *
import random

def shutDown():
	global gameOver
	gameOver = True

def showHelp():
	print()
	print('=================================')
	print('=      Available commands       =')
	print('=================================')
	print('<coords> <value> | e.g a1 1      ')
	print('solve                            ')
	print('help                             ')
	print('exit                             ')
	print('=================================')



newBoard = SudokuBoard()

commands = {"solve" : newBoard.solve, "help" : showHelp, "exit" : shutDown}

gameOver = False
while gameOver == False:

	newBoard.printBoard()
	
	userInput = input("??? ").split()

	if len(userInput) == 0:
		pass

	elif len(userInput) == 1:
		commands[userInput[0]]()

	elif len(userInput) == 2:
		x, y = (ord(userInput[0][0]) - 97), (int(userInput[0][1]) - 1)
		i = int(userInput[-1])
		if newBoard.checkValidPlacement((x, y), i) == True:
			newBoard.placeValue((x, y), i)
		else:
			print("\nInvalid placement.")

	else:
		print("\nInvalid command.")