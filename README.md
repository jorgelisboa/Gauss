# The Gauss-Seidel method

##### The Gauss-Seidel method is an iterative method for solving systems of linear equations.

## How does GaussSeidel method works?
- See if our equation is possible to resolve.
- Change array ord until there is no zeros in the main diagonal.
- Turn the main diagonal element into **1**, dividing all the numbers for the first one.

  | 4 | 0 | 2 | 24 |
  |---|---|---|---|
  | 2 | 3 | 0 | 16 |
  | 0 | 3 | 2 | 28 |
  
  | 1 | 0 | 1/2 | 6 |
  |---|---|---|---|
  | 2 | 3 | 0 | 16 |
  | 0 | 3 | 2 | 28 |

- Now, we need to set the rest of our column to zero
  - Get the number in the column that you want to turn into zero (if it's already 0, don't do nothing and go to the next line), for example **2**
  - Multiply by **-1**
  - Get the **-2** and multiply the line that you just put **1**
  - | -2 | 0 | -1 | -12 |
  - Now, sum the line that you want to set zero by the line that you generated
- Now you will see something like this
  | 1 | 0 | 1/2 | 6 |
  |---|---|---|---|
  | 0 | 3 | -1 | 4 |
  | 0 | 3 | 2 | 28 |

- Continue doing this, line by line and you will have something like at the end
  | 1 | 0 | 0 | 2 |
  |---|---|---|---|
  | 0 | 1 | 0 | 4 |
  | 0 | 0 | 1 | 6 |
  
