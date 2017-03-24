import random

class matrixOps:
	def __init__(self, matrix):
		self.matrix = matrix
		self.magicSum = []
	
	#check if all items in given array are equal
	def checkEquality(self):
		if self.magicSum.count(self.magicSum[0]) == len(self.magicSum):
			return True
		else:
			return False
	
	#generate a random matrix with inputted length
	def generateRandom(self, length):
		newMatrix = []
		
		for i in range(length):
			row = []
			
			for j in range(length):
				row.append(random.randint())
			
			newMatrix.append(row)
		
		self.matrix = newMatrix
		print("Random matrix generated successfully! ")
	
	def maxRow(self):
		length = len(self.matrix)
		maxRow = 0
		
		for i in self.matrix:
			rowSum = 0
			
			for j in i:
				rowSum += i
			
			if maxRow < rowSum:
				maxRow = rowSum
			else:
				pass
	
	#check if the sums of numbers in each row are equal
	def checkRows(self):
		length = len(self.matrix)
		
		for i in range(length):
			itemSum = 0
			array = self.matrix[i]

			for j in array:
				itemSum += j

			self.magicSum.append(itemSum)
	
	#check if the sums of numbers in each column are equal
	def checkCols(self):
		length = len(self.matrix)

		for i in range(length):
			itemSum = 0
			
			for j in self.matrix:
				itemSum += j[i]

			self.magicSum.append(itemSum)

	#check if the sums of numbers in both diagonals are equal
	def checkDiag(self):
		length = len(self.matrix)
		diag1 = 0
		diag2 = 0

		for i in range(length):
			diag1 += self.matrix[i][i]

		for i in range(length):
			diag2 += self.matrix[length-1-i][i]

		self.magicSum.extend([diag1, diag2])

#lets user to input a matrix aka the magic square
def inputMatrix():
	matrix = []
	c = int(input("How big are the square's sides? "))
	
	for i in range(c):
		row = []
		for j in range(c):
			r = int(input("Insert the number from coordinate ["+str(i)+"]["+str(j)+"]: "))
			row.append(r)
		matrix.append(row)
		
	return matrix

M = inputMatrix()

Matrix = matrixOps(M)
Matrix.checkCols()
Matrix.checkDiag()
Matrix.checkRows()

#check if the given matrix of numbers makes up a magic square
if Matrix.checkEquality():
    print("The square is truly tremendous!")
else:
    print("The square is a complete letdown, not unlike yourself.")

input("Press enter to exit..")
