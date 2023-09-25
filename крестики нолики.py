def tic_tac_toe(field):
    for i in field:
        if i[0] == i[1] == i[2] == "x":
            print("x win")
            return
        elif i[0] == i[1] == i[2] == "0":
            print("0 win")
            return
    if field[0][0] == field[1][1] == field[2][2] == "x":
        print("x win")
        return
    if field[0][0] == field[1][1] == field[2][2] == "0":
        print("0 win")
        return
    if field[0][2] == field[1][1] == field[2][0] == "0":
        print("0 win")
        return
    if field[0][2] == field[1][1] == field[2][0] == "x":
        print("x win")
        return
    if field[0][0] == field[1][0] == field[2][0] == "x":
        print("x win")
        return
    if field[0][1] == field[1][1] == field[2][1] == "x":
        print("x win")
        return
    if field[0][2] == field[1][2] == field[2][2] == "x":
        print("x win")
        return
    if field[0][0] == field[1][0] == field[2][0] == "0":
        print("x win")
        return
    if field[0][1] == field[1][1] == field[2][1] == "0":
        print("x win")
        return
    if field[0][2] == field[1][2] == field[2][2] == "0":
        print("x win")
        return
    print("draw")
