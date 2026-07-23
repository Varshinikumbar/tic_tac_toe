def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"

    def display_board():
        print("\n")
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("\n")

    def check_winner(player):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for pattern in win_patterns:
            if all(board[pos] == player for pos in pattern):
                return True
        return False

    def is_draw():
        return " " not in board

    print("=== TIC-TAC-TOE GAME ===")
    print("Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nType 'q' anytime to quit.\n")

    while True:
        display_board()

        move = input(f"Player {current_player}, enter position (1-9) or 'q': ").strip()

        if move.lower() == "q":
            print("\nGame Quit Successfully!")
            break

        if not move.isdigit():
            print("Invalid input! Enter a number from 1 to 9.")
            continue

        position = int(move)

        if position < 1 or position > 9:
            print("Position must be between 1 and 9.")
            continue

        if board[position - 1] != " ":
            print("Position already occupied. Try another one.")
            continue

        board[position - 1] = current_player

        # Show current state after every move
        print("\nCurrent Game State:")
        display_board()

        if check_winner(current_player):
            print(f"🎉🎉 Congratulations! Winner is '{current_player}' ⭐🏆 🎉🎉")
            break

        if is_draw():
            print("🤝 Game Draw! No Winner.")
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()