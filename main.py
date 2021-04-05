N = 3

def scan_board(board):
    rows = [0,0,0]
    cols = [0,0,0]
    diagonals = [0,0]
    
    for i in range(N):
        for j in range(N):
            rows[i] += board[i][j] if board[i][j] != 2 else -1 # count rows
            cols[j] += board[j][i] if board[j][i] != 2 else -1 # count columns
        
        # main diagonal
        diagonals[0] += board[i][i] if board[i][i] != 2 else -1 
        
        #secondary digonal
        diagonals[1] += board[N-1-i][i] if board[N-1-i][i] != 2 else -1
    
    return rows + cols + diagonals
 

game = [[1,2,0],
        [2,1,0],
        [2,1,1]]
 
print(scan_board(game))
