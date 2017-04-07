def printAsMatrix(matrix):
    for i in matrix:
        print(i)
    print("\n")

def generateChessBoard(matrix):
    for i in range(8):
        array = []

        for j in range(8):
            array.append(0)
        
        matrix.append(array)

    return matrix

def checkRC(matrix, posX, posY):
    for i in range(8):
        matrix[posY][i] = 1
        
    for i in range(8):
        matrix[i][posX] = 1

def checkDiag1(matrix, posX, posY):
    x = posX
    y = posY

    while x and y > 0:
        x-=1
        y-=1
        
    if x == 0:
        for i in range(8-y):
            matrix[y][x] = 1
            x+=1
            y+=1
            
    elif y == 0:
        for i in range(8-x):
            matrix[y][x] = 1
            x+=1
            y+=1

def checkDiag2(matrix, posX, posY):
    x = posX
    y = posY

    while x > 0 and y < 7:
        x-=1
        y+=1

    if x == 0:
        while y >= 0:
            matrix[y][x] = 1
            x+=1
            y-=1

    elif y == 7:
        while x <= 7:
            matrix[y][x] = 1
            x+=1
            y-=1

M = []
generateChessBoard(M)

sis = open("lipp.sis", "r")
reps = int(sis.readline())

for i in range(reps):
    chesspos = sis.readline()
    print(chesspos)
    posX = ord(chesspos[0])-97
    posY = 8-int(chesspos[1])

    checkRC(M, posX, posY)
    checkDiag1(M, posX, posY)
    checkDiag2(M, posX, posY)

    printAsMatrix(M)
