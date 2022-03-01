# is Safe function to walk to safest path called by solveNQUntil function for each col
def isSafe(board, row, col):   
    for i in range(col):
      # if board[row][i] is 1 then backtrack and return false 
        if board[row][i] == 1: 
            return False  
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False  
    return True
  
  def solveNQUtil(board, col): 
      
    if col >= N: 
        return True
  
    for i in range(N): 
  
        if isSafe(board, i, col):               
            board[i][col] = 1
  
            if solveNQUtil(board, col + 1) == True: 
                return True
  
            board[i][col] = 0

    return False
  
  def solveNQ(): 
    if solveNQUtil(board, 0) == False: 
        print ("Solution does not exist") 
        return False
  
    printSolution(board) 
    return True
  
  board = [[0] * N for i in range(N)]
board



global N
# N is number of rows and coloumns 
N = 4
#print solution to generate a chess board of possible solution
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print()
