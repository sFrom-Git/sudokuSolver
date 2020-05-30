class SudokuBoard:

	def __init__(self):
		self.board = [
		[0,0,0,0,0,0,0,0,0], #1
		[0,0,0,0,0,0,0,0,0], #2
		[0,0,0,0,0,0,0,0,0], #3
		[0,0,0,0,0,0,0,0,0], #4
		[0,0,0,0,0,0,0,0,0], #5
		[0,0,0,0,0,0,0,0,0], #6
		[0,0,0,0,0,0,0,0,0], #7
		[0,0,0,0,0,0,0,0,0], #8
		[0,0,0,0,0,0,0,0,0]  #9
		]
		#a b c d e f g h i

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


	def insertValue(self, position, value):
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
			print(self.board[self.currentQuad[i][1]][self.currentQuad[i][0]])
			if value == self.board[self.currentQuad[i][1]][self.currentQuad[i][0]]:
				return False
				
		self.board[y][x] = value
		return True

	def returnValue(self):
		return self.board
