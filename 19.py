def correct_move(move):
    # без проверки на флоат и возможность хода. Просто корректный символ
    if len(move) == 4 and move.isdigit() is True and 1 <= int(move[0]) <= 3 and 1 <= int(move[1]) <= 9:
        return True

def move_maker(move):
    # получаем координаты клеток из строки с ходом
    x1 = int(move[0]) - 1
    y1 = int(move[1]) - 1
    x2 = int(move[2]) - 1
    y2 = int(move[3]) - 1
    # проверка на то стоят ли рядом выбранные клетки и равны ли они или в сумме дают 10
    if ((abs(y2 - y1) == 1 and x1 == x2) or (abs(x2 - x1) == 1 and y1 == y2)) and (int(board[x1][y1]) + int(board[x2][y2]) == 10 or int(board[x1][y1]) == int(board[x2][y2])):
        board[x1].pop(y1)
        board[x2].pop(y2) # удаляем элементы
        print("Вычеркнуто!")

        # Деоаем сдвиг поля, тк 2 элемента вычеркнуты
        # новое количество элментов в списке(до этого было 27)
        new_len = 0
        for i in board:
            new_len += len(i)
        print(new_len)
        # создаем вспомогательное поле в которое соберем все оставшиеся элементы
        help_board = []
        for i in board:
            for j in i:
                help_board.append(j)
        # очистим основное поле и заполним его заново
        board.clear()
        for i in range(len(help_board)):
            if new_len == 18: # если всего 18 эоементов осталось то нужно просто добавить две линии в поле
                board.append(help_board[0:10])
                board.append(help_board[9:19])
            elif new_len == 9: # если всего 9 эоементов осталось то нужно просто добавить одну линию в поле
                board.append(help_board)
            else: # если количество не кратно 9 нужно записать полную строку(строки) а остаток перекинуть на следующую
                k_9 = 0
                for i in range(new_len // 9) : # new_len // 9 деление нацело даст количество строк которые мы сможем при текущей длине заполнить цифрами до 9 элементов в строке
                    board.append(help_board[k_9:k_9+10]) # lобавляем с 0 по 0+10 элемента и потом с 9 элемента до 9+10 элемента
                    k_9 += 9 
                board.append(help_board[(new_len//9*9 + 1)::]) # добавляем остаток не заполняющий строку до 9
            # print(board)
        return board # возвращаем обновленную строку
        """
        # count += 1
        # return count """

        
def win_check(board): # проверка на конец игры, не доработана
    for i in range(len(board)):
        for j in range(len(board[i])):
            if "#" not in board[i][j]:
                return False
    return True


# игровое поле
board = [["1", "2", "3", "4", "5", "6", "7", "8", "9"],
         ["1", "1", "1", "2", "1", "3", "1", "4", "1"],
         ["5", "1", "6", "1", "7", "1", "8", "1", "9"]]

print("Игра 19")
print("Ввод координат клеток: номер строки и номер столбца 1 клетки и 2 клетки слитно(1-3; 1-9)")
print("Пример: 1112 (клетка(1, 1) и клетка (1,2))")
name1 = input("Первый игрок: ")
name2 = input("Второй игрок: ")
k = 1
count = 0

while True: # основной игровой цикл

    
    """if win_check(board):
        if k % 2 != 0:
            print("win, ", name1)
            break
        elif k % 2 == 0:
            print("win, ", name2)
            break"""
    if len(board) == 0:
        print("win") # Злесь реализовать проверку на победителя

    for i in range(len(board)): # вывод игрового поля
        print(" ".join(board[i]))

    if k % 2 != 0: # ход первого
        while True:
            move = input(f"{name1}, сделайте ход: ")
            if correct_move(move) is True:
                break
        move_maker(move)
        k += 1

    elif k % 2 == 0: # ход второго
        while True:
            move = input(f"{name2}, сделайте ход: ")
            if correct_move(move) is True:
                break
        move_maker(move)
        k += 1
