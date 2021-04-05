N = 3
player_values = [0, 1, -1]

def scan_board(board):
    rows = [0,0,0]
    cols = [0,0,0]
    diagonals = [0,0]
    
    for i in range(N):
        for j in range(N):
            rows[i] += player_values[board[i][j]] # count rows
            cols[i] += player_values[board[j][i]] # count columns
        
        # main diagonal
        diagonals[0] += player_values[board[i][i]]
        
        #secondary digonal
        diagonals[1] += player_values[board[N-1-i][i]]
    
    return rows + cols + diagonals
 

game = [[1,2,0],
        [2,1,0],
        [2,1,1]]
 
counters = scan_board(game)

is_tie = True
for counter in counters:
    if (counter == 3):
        print("player 1 won")
        is_tie = False
        break
    
    if (counter == -3):
        print("player 2 won")
        is_tie = False
        break
        
if (is_tie):
    print("tie")
