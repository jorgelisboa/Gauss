# Variables
matriz = [[2,3,5,1], [9,2,6,7], [3,6,2,9]]

# Check if it is possible
def hasZeroInDiagonal (matriz):
    qtdDeZeros=0
    posicao=0
    while posicao<len(matriz):
        if matriz[posicao][posicao]==0: 
            qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
    
def setOneInMainDiagonal (line,matriz):
    divisor=matriz[line][line]
    col=0
    while col<=len(matriz):
        matriz[line][col]/=divisor
        col+=1

# APP STARTS HERE #   
def startApp():
    # Check if is possible to resolve the system
    if isSystemPossible():
        if hasZeroInDiagonal(matriz):
            changeLines(matriz)
        else:
            resolveSystem(matriz)
            showMatriz(matriz)
    else:
        print("This system is not possible to be resolved")

def resolveSystem(matriz):
    currentLine = 0
    while currentLine < len(matriz):
        setOneInMainDiagonal(matriz, currentLine)
        setZeroInColumn(matriz, currentLine)

def showMatriz(matriz):
    counter = 0
    while counter < len(matriz):
        print(matriz[[counter]])

showMatriz(matriz)
