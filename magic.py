#check if all items in given array are equal
def checkEquality(array):
    if array.count(array[0]) == len(array):
        return True
    else:
        return False

#lets user to input a matrix aka the magic square
def inputMatrix(matrix):
    c = int(input("How big are the square's sides? "))
    
    for i in range(c):
        row = []
        for j in range(c):
            r = int(input("Insert the number from coordinate ["+str(i)+"]["+str(j)+"]: "))
            row.append(r)
        matrix.append(row)
        
    return matrix

#check if the sums of numbers in each row are equal
def checkRows(matrix):
    length = len(matrix)
    magicRows = []
    
    for i in range(length):
        itemSum = 0
        array = matrix[i]

        for j in array:
            itemSum += j

        magicRows.append(itemSum)

    return checkEquality(magicRows)

#check if the sums of numbers in each column are equal
def checkCols(matrix):
    length = len(matrix)
    magicCols = []

    for i in range(length):
        itemSum = 0
        
        for j in matrix:
            itemSum += j[i]

        magicCols.append(itemSum)

    return checkEquality(magicCols)

#check if the sums of numbers in both diagonals are equal
def checkDiag(matrix):
    length = len(matrix)
    diag1 = 0
    diag2 = 0

    for i in range(length):
        diag1 += matrix[i][i]

    for i in range(length):
        diag2 += matrix[length-1-i][i]

    if diag1 == diag2:
        return True
    else:
        return False

M = []
M = inputMatrix(M)
#check if the given matrix of numbers makes up a magic square
if checkRows(M) and checkCols(M) and checkDiag(M):
    print("The square is truly tremendous!")
else:
    print("The square is a complete letdown, not unlike yourself.")
