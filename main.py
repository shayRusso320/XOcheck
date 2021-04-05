N = 3
PLAYERS_VALUES = [0, 1, -1]

def scan_board(board):
    rows = [0,0,0]
    cols = [0,0,0]
    diagonals = [0,0]
    
    for i in range(N):
        for j in range(N):
            rows[i] += PLAYERS_VALUES[board[i][j]] # count rows
            cols[j] += PLAYERS_VALUES[board[j][i]] # count columns
        
        # main diagonal
        diagonals[0] += PLAYERS_VALUES[board[i][i]]
        
        #secondary digonal
        diagonals[1] += PLAYERS_VALUES[board[N-1-i][i]]
    
    return rows + cols + diagonals
 

game = [[1,2,0],
        [2,1,0],
        [2,1,1]]
 
print(scan_board(game))
