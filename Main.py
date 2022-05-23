# função auxiliar  recursiva que, de fato, gera as permutacoes
# NÃO USE DIRETAMENTE ESTA FUNÇÃO; USE A FUNÇÃO permutacoes
# recebe uma lista com os valores a serem permutados (linha),
# uma lista com os itens na permutação sendo gerada (perm) e
# uma lista com as permutações geradas (perms) 
def permuta (linha, perm, perms):
    if linha==[]:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin]+linha[lin+1:len(linha)],perm+[linha[lin]],perms)

# função principal para gerar permutações;
# USA A FUNÇÃO permuta, QUE NÃO DEVE SER USADA DIRETAMENTE;
# recebe uma lista com os valores a serem permutados (linha)
# retorna as permutações geradas
def permutacoes (linha):
    perms=[]
    permuta(linha,[],perms)
    return perms
    
def haZeroNaDiagonal (m,ordL,ordC):
    qtdDeZeros=0
    posicao=0
    while posicao<len(m):
        if m[ordL[posicao]][ordC[posicao]]==0: qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
   
def comoSeLivrarDeZerosNaDiagonal (m):
    perms = permutacoes(list(range(len(m))))

    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(m,perms[i],perms[j]):
                return [perms[i],perms[j]];

# "Divide" os pares de linha - (Já tá fazendo os pares, falta dividor)

def isMatrizValida(matriz):
    #todas as linhas com a mesma quantidade de coluna
    currentLine = 0
    compareLine = 0
    currentColumn = 0
    resultLine = [] 
    isValida = True
    while currentLine < len(matriz): #percorre as linhas
        compareLine = currentLine + 1
        while compareLine < len(matriz):
            currentColumn = 0
            resultLine = []
            while currentColumn < (len(matriz[currentLine])-1): # percorre coluna da linha atual
                if matriz[compareLine][currentColumn] == 0: 
                    result = 999999
                else:
                    result = matriz[currentLine][currentColumn] / matriz[compareLine][currentColumn]
                print(currentLine, ' linha ', matriz[currentLine][currentColumn],'linha', compareLine, " ", matriz[compareLine][currentColumn])
                print(result)
                resultLine.append(result)
                print("result line = ", resultLine)
                currentColumn +=1
            compareLine +=1
        currentLine +=1
    return isValida;

##################################################################################################
def negativeLine(lineMatriz):
    counter = 0
    while counter < len(lineMatriz):
        lineMatriz[counter] = lineMatriz[counter]-1
        counter += 1
    return lineMatriz

# Our matriz

def setZeroInColumn(matriz, currentColumn):
    currentLine = 0
    matrizAux = matriz.copy() 
    compareLine = negativeLine(matrizAux[currentColumn -1])
    while currentLine < len(matriz):
        if matriz[currentLine][currentColumn] != 0:
#            matriz[compareLine] = matriz[line] -1
#            print("compare line: ", compareLine)
            print("linha que divide: ", compareLine)
            print("minha matriz: ", matriz)
            print("item da coluna pra ser dividid0 = ", matriz[currentLine][currentColumn])
        currentLine+=1

# Check if it is possible
def hasZeroInDiagonal (matriz):
    qtdDeZeros=0
    posicao=0
    while posicao<len(matriz):
        if matriz[posicao][posicao]==0: 
            qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
  
    
def isMatrizValida(matriz):
    #todas as linhas com a mesma quantidade de coluna
    currentLine = 0
    compareLine = 0
    currentColumn = 0
    resultLine = [] 
    isValida = True
    while currentLine < len(matriz): #percorre as linhas
        compareLine = currentLine + 1
        while compareLine < len(matriz):
            currentColumn = 0
            resultLine = []
            while currentColumn < (len(matriz[currentLine])-1): # percorre coluna da linha atual
                if matriz[compareLine][currentColumn] == 0: 
                    result = 999999
                else:
                    result = matriz[currentLine][currentColumn] / matriz[compareLine][currentColumn]
                print(currentLine, ' linha ', matriz[currentLine][currentColumn],'linha', compareLine, " ", matriz[compareLine][currentColumn])
                print(result)
                resultLine.append(result)
                print("result line = ", resultLine)
                currentColumn +=1
            compareLine +=1
        currentLine +=1
    return isValida;
# Make the logic: make the main diagonal number became 1, and after this, set zero in all the column
def setOneInMainDiagonal (line,matriz):
    divisor=matriz[line][line] # Get our main diagonal number
    col=0
    while col<=len(matriz): # Will divide each item from our line for our main diagonal number
        matriz[line][col]/=divisor
        print("setOneInMainDiagonal: "+str(matriz))
        col+=1
    return matriz


# APP STARTS HERE #   

def changeLines(matriz):
    counter = 0
    ordemMatriz = comoSeLivrarDeZerosNaDiagonal(matriz)
    matrizZerada = []
    while counter < len(ordemMatriz[1]):
        matrizZerada.append(matriz[ordemMatriz[1][counter]])
        counter+=1
    return matrizZerada
      
def resolveSystem(matriz):
    currentLine = 0
    while currentLine < len(matriz):
        setOneInMainDiagonal(currentLine, matriz)
        #setZeroInColumn(matriz, currentLine)
        currentLine += 1
        
def showMatriz(matriz):
    counter = 0
    while counter < len(matriz):
        print(matriz[[counter]])
        
# Check if is possible to resolve the system
matriz = [[0,3,2,28], [4,0,2,24], [2,3,0,16]]
def startApp(matriz):
    isSystemPossible = True
    if isSystemPossible:
        if hasZeroInDiagonal(matriz):
            while hasZeroInDiagonal(matriz):
                changeLines(matriz)
                matriz = changeLines(matriz)
                resolveSystem(matriz)
                #showMatriz(matriz)
        else:
            resolveSystem(matriz)
            #showMatriz(matriz)
    else:
        print("This system is not possible to be resolved")
            
startApp(matriz)
