# Gauss
System to solve systems of linear equations with any number of equations by the method of GaussSeidel.

## How does GaussSeidel method works?

- See if our equation is possible to resolve.
- Change array ord until there is no zeros in the main diagonal.
- Turn the 1° element of the first line in **1**, dividing all the numbers for the first one.
  | 4 | 0 | 2 | 24 |
  |---|---|---|---|
  | 2 | 3 | 0 | 16 |
  | 0 | 3 | 2 | 28 |
  
  | 1 | 0 | 1/2 | 6 |
  |---|---|---|---|
  | 2 | 3 | 0 | 16 |
  | 0 | 3 | 2 | 28 |
  - Divide the 


### Workflow
- validateMatriz(matriz)
- diagonalHasZero(matriz, lenght(matriz))
- if diagonalHasZero() { changeLines(matriz, matrizLine) } else { divideLine(matrizLine, divider) }
- startLoop()
- divideLine()

Após colocar 1 na diagonal principal, vá para a próxima linha, pegue o primeiro número (se não for 0) e multiplique por -1, multiplique a linha que você colocou 1 pelo número que você negativou. Depois, vá para a linha que deseja implantar 0 e some-as. Faça isso até a útlima linha.
