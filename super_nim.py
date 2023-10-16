import random

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))

def get_user_input():
    while True:
        try:
            row = int(input("Введите номер строки: "))
            col = int(input("Введите номер столбца: "))
            return row, col
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")

def is_game_over(board):
    return all(all(cell == 0 for cell in row) for row in board)

def play_game():
    rows = 5
    cols = 5

    board = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    player = 1

    while not is_game_over(board):
        print_board(board)
        print(f"Ход игрока {player}")

        row, col = get_user_input()

        if row < 1 or row > rows or col < 1 or col > cols:
            print("Некорректные координаты. Попробуйте еще раз.")
            continue

        row -= 1
        col -= 1

        if all(cell == 0 for cell in board[row]):
            print("На выбранной строке нет фишек. Попробуйте еще раз.")
            continue

        if all(row[col] == 0 for row in board):
            print("На выбранном столбце нет фишек. Попробуйте еще раз.")
            continue

        board[row] = [0] * cols
        for i in range(rows):
            board[i][col] = 0

        player = 3 - player

    print_board(board)
    print(f"Игрок {player} победил!")

play_game()
