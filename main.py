def print_board(board):
    # Вывод доски на консоль
    for row in board:
        print(*row)

def check_right(board, idx):
    # Проверка, что ячейка свободна
    try:
        if board[int(idx[0])+1][int(idx[1])+1] == "-":
            return True
    except:
        pass
    return False

def change_board(board, idx, cur_player):
    # Внесение изменений на доску
    board[int(idx[0])+1][int(idx[1])+1] = str(cur_player).replace("1", "x").replace("2", "o")
    return board

def cur_player_is_win(board, cur_player):
    # Проверка, победил ли текущий игрок?
    s = str(cur_player).replace("1", "x").replace("2", "o")*3

    if board[1][1] + board[1][2] + board[1][3] == s or \
           (board[2][1]+board[2][2]+board[2][3]) == s or \
           (board[3][1]+board[3][2]+board[3][3]) == s or \
           (board[1][1] + board[2][1] + board[3][1]) == s or \
           (board[1][2] + board[2][2] + board[3][2]) == s or \
           (board[1][3] + board[2][3] + board[3][3]) == s or \
           (board[1][1] + board[2][2] + board[3][3]) == s or \
           (board[3][1] + board[2][2] + board[1][3]) == s:
        return True
    else:
        return False

def main():
    # Инициализация пустой доски
    board = [[" ", 0, 1, 2],[0, "-", "-", "-"],[1, "-", "-", "-"],[2, "-", "-", "-"]]
    # Первым ходит игрок 1 (X)
    cur_player = 1
    idx = "xo"
    while True:
        # Вывод текущего состояни доски в консоль
        print_board(board)
        # Проверку правильности хода
        while not check_right(board, idx):
            # Делаем ход
            idx = input(f"Игрок {cur_player} , введите индекс ячейки в виде двух цифр - Номер строки и Номер столбца:")

        # Внести изменения в доску
        board = change_board(board, idx, cur_player)
        # Проверка, что текущий игрок выиграл
        if cur_player_is_win(board, cur_player):
            print_board(board)
            print(f"Победил игрок {cur_player}")
            break
        # Смена хода
        if cur_player == 1:
            cur_player = 2
        else:
            cur_player = 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()