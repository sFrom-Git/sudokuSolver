class SudokuBoard:

	def __init__(self):
		self.board = [
		[1,0,0,0,0,0,0,0,0], #1
		[0,0,0,0,0,0,0,0,0], #2
		[0,0,0,0,0,0,0,0,0], #3
		[0,0,0,0,0,0,0,0,0], #4
		[0,0,0,0,0,7,0,0,0], #5
		[0,0,0,0,0,0,0,0,0], #6
		[0,0,2,0,0,0,0,0,0], #7
		[0,0,0,0,0,0,0,0,0], #8
		[0,0,0,0,0,0,0,0,0]  #9
		]
		#a b c d e f g h i

		#This is some hardcoded spaghett
		self.quadrants = [
		[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)], #q1
		[(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)], #q2
		[(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)], #q3
		[(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)], #q4
		[(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)], #q5
		[(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)], #q6
		[(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)], #q7
		[(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)], #q8
		[(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]  #q9
		]

	def solve(self):
		for y in range(0,9):
			for x in range(0,9):
				if self.board[y][x] == 0:
					for i in range(1,10):
						if self.checkValidPlacement((x, y), i):
							self.board[y][x] = i
							self.solve()
							self.board[y][x] = 0
					return
		self.printBoard()
		terminate = input("Stop? Y/N ")
		if terminate == 'y' or terminate == 'Y':
			exit()
		elif terminate == 'n' or terminate == 'N':
			pass
		else:
			pass

		
	def placeValue(self, position, value):
		x = position[0]
		y = position[1]
		self.board[y][x] = value
		return

	def checkValidPlacement(self, position, value):
		x = position[0]
		y = position[1]

		#Scan horizontally
		for i in range(9):
			if self.board[y][i] == value:
				return False

		#Scan vertically
		for i in range(9):
			if self.board[i][x] == value:
				return False

		#Find which quadrant we're in
		for i in range(len(self.quadrants)):
			if position in self.quadrants[i]:
				self.currentQuad = self.quadrants[i]

		#Scan the quadrant
		for i in range(len(self.currentQuad)):
			if value == self.board[self.currentQuad[i][1]][self.currentQuad[i][0]]:
				return False
				
		return True

	def returnValue(self):
		return self.board

	def printBoard(self):
		print()
		print("    a  b  c   d  e  f   g  h  i")
		print("   _____________________________")
		print("1 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 1".format(self.board[0][0],self.board[0][1],self.board[0][2],self.board[0][3],self.board[0][4],self.board[0][5],self.board[0][6],self.board[0][7],self.board[0][8]))
		print("2 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 2".format(self.board[1][0],self.board[1][1],self.board[1][2],self.board[1][3],self.board[1][4],self.board[1][5],self.board[1][6],self.board[1][7],self.board[1][8]))
		print("3 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 3".format(self.board[2][0],self.board[2][1],self.board[2][2],self.board[2][3],self.board[2][4],self.board[2][5],self.board[2][6],self.board[2][7],self.board[2][8]))
		print("  |-----------------------------|")
		print("4 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 4".format(self.board[3][0],self.board[3][1],self.board[3][2],self.board[3][3],self.board[3][4],self.board[3][5],self.board[3][6],self.board[3][7],self.board[3][8]))
		print("5 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 5".format(self.board[4][0],self.board[4][1],self.board[4][2],self.board[4][3],self.board[4][4],self.board[4][5],self.board[4][6],self.board[4][7],self.board[4][8]))
		print("6 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 6".format(self.board[5][0],self.board[5][1],self.board[5][2],self.board[5][3],self.board[5][4],self.board[5][5],self.board[5][6],self.board[5][7],self.board[5][8]))
		print("  |-----------------------------|")
		print("7 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 7".format(self.board[6][0],self.board[6][1],self.board[6][2],self.board[6][3],self.board[6][4],self.board[6][5],self.board[6][6],self.board[6][7],self.board[6][8]))
		print("8 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 8".format(self.board[7][0],self.board[7][1],self.board[7][2],self.board[7][3],self.board[7][4],self.board[7][5],self.board[7][6],self.board[7][7],self.board[7][8]))
		print("9 | {}  {}  {} | {}  {}  {} | {}  {}  {} | 9".format(self.board[8][0],self.board[8][1],self.board[8][2],self.board[8][3],self.board[8][4],self.board[8][5],self.board[8][6],self.board[8][7],self.board[8][8]))
		print("   =============================")
		print("    a  b  c   d  e  f   g  h  i")
		print()