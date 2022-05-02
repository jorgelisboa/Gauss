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
