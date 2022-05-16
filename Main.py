# Our matriz
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
  
# Make the logic: make the main diagonal number became 1, and after this, set zero in all the column
def setOneInMainDiagonal (line,matriz):
    divisor=matriz[line][line] # Get our main diagonal number
    col=0
    while col<=len(matriz): # Will divide each item from our line for our main diagonal number
        matriz[line][col]/=divisor
        print(matriz)
        col+=1


# APP STARTS HERE #   
def startApp():
    # Check if is possible to resolve the system
    if isSystemPossible():
        if hasZeroInDiagonal(matriz):
            while hasZeroInDiagonal(matriz):
                changeLines(matriz)
            resolveSystem(matriz)
            showMatriz(matriz)
        else:
            resolveSystem(matriz)
            showMatriz(matriz)
    else:
        print("This system is not possible to be resolved")

def changeLines(matriz):
    matriz.insert(0, matriz[-1])
    matriz.pop() #Without argument, it takes -1 as default
      
def resolveSystem(matriz):
    currentLine = 0
    while currentLine < len(matriz):
        setOneInMainDiagonal(currentLine, matriz)
        setZeroInColumn(matriz, currentLine)
        currentLine += 1
        
def showMatriz(matriz):
    counter = 0
    while counter < len(matriz):
        print(matriz[[counter]])

showMatriz(matriz)
