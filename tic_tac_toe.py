def print_board(board):
    print(f"""
     {board[0]} | {board[1]} | {board[2]}  
    ---+---+--- 
     {board[3]} | {board[4]} | {board[5]}  
    ---+---+--- 
     {board[6]} | {board[7]} | {board[8]}  
    """)

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns 
        [0, 4, 8], [2, 4, 6]              # Diagonals 
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def tic_tac_toe():
    sets = int(input("Enter the number of sets to play: "))
    x_wins, o_wins, draws = 0, 0, 0
    
    for game in range(sets):
        print(f"\nStarting Set {game + 1} of {sets}\n")
        board = [' ' for _ in range(9)]
        current_player = 'X'
        print_board(board)
        
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
                
                board[move] = current_player
                print_board(board)
                
                if check_winner(board, current_player):
                    print(f"Player {current_player} wins Set {game + 1}!")
                    if current_player == 'X':
                        x_wins += 1
                    else:
                        o_wins += 1
                    break
                
                if is_draw(board):
                    print("It's a draw!")
                    draws += 1
                    break
                
                current_player = 'O' if current_player == 'X' else 'X'
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
    
    print("\nGame Over!")
    print(f"Final Score: X Wins: {x_wins}, O Wins: {o_wins}, Draws: {draws}")

if __name__ == "__main__":
  tic_tac_toe()
