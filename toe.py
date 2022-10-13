import random
a = "_________"
xy = [0, 1, 2]
game = [[a[i] for i in range(3)], [a[i] for i in range(3, 6)], [a[i] for i in range(6, 9)]]
def printer():
    print("---------")
    for i in game:
        print("| " + " ".join(i) + " |")
    print("---------")
def easy(w,msg=True):
    global game
    if msg:
        print('Making move level "easy"')
    while True:
        x = random.choice(xy)
        y = random.choice(xy)
        if game[x][y] == "_":
            return move(x, y, w)
def medium(w, msg=True):
    global game
    if msg:
        print('Making move level "medium"')

    for i, j, k in zip([0,1, 2], [1, 2, 0], [2, 0, 1]):
        for p in xy:
            if game[p][i] == game[p][j] != "_" and game[p][k] == "_":
                return move(p, k, w)
            if game[i][p] == game[j][p] != "_" and game[k][p] == "_":
                return move(k, p, w)
        if game[i][i] == game[j][j] != "_" and game[k][k] == "_":
            return move(k, k, w)
        if game[2 - i][i] == game[2 - j][j] != "_" and game[2 - k][k] == "_":
            return move(2 - k, k, w)
    if not msg:
        if game[1][1] == "_":
            return move(1, 1, w)
        for i, j, k in zip([0,1, 2], [2, 0, 1], [1, 2, 0]):
            for p in xy:
                if game[p][i] == game[p][j] != "_" and game[p][k] == "_":
                    return move(p, k, w)
                if game[i][p] == game[j][p] != "_" and game[k][p] == "_":
                    return move(k, p, w)

            if game[i][i] == game[j][j] != "_" and game[k][k] == "_":
                return move(k, k, w)
            if game[2 - i][i] == game[2 - j][j] != "_" and game[2 - k][k] == "_":
                return move(2 - k, k, w)
            for p in xy:
                if game[p][i] == "_" and game[p][k] == w and game[p][j] == "_":
                    return move(p, j, w)
                if game[i][p] == "_" and game[k][p] == w and game[j][p] == "_":
                    return move(k, p, w)
            for m, n in zip([0, 1, 1, 2], [1, 0, 2, 1]):
                if game[m][n] == "_":
                    return move(m, n, w)


    return easy(w, False)
def hard(w):
    print('Making move level "hard"')
    return medium(w, False)


def move(r, c, w):
    global game, turn
    game[r][c] = w
    printer()
    resulto = result()
    if resulto == "continue":
        return False
    else:
        print(resulto)
    return True
def result():
    win = ""
    x_num = 0
    o_num = 0
    _num = 0
    for r in xy:
        for c in xy:
            i = game[r][c]
            if i == "X":
                x_num += 1
            elif i == "O":
                o_num += 1
            else:
                _num += 1
    for i in "XO":
        for r in xy:
            if game[r][0] == game[r][1] == game[r][2] == i:
                win += i
            if game[0][r] == game[1][r] == game[2][r] == i:
                win += i
        if game[0][0] == game[1][1] == game[2][2] == i:
            win += i
        if game[0][2] == game[1][1] == game[2][0] == i:
            win += i
    if len(win) == 0:
        if _num != 0:
            return "continue"
        else:
            return "Draw"
    else:
        return f"{win[0]} wins"
def user(w):
    while True:
        cord = input("Enter the coordinates: ")
        try:
            r, *m, c = cord
            r = int(r) - 1
            c = int(c) - 1
            if game[r][c] == "_":
                return move(r, c, w)
            else:
                print("This cell is occupied! Choose another one!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")
        except Exception:
            print("You should enter numbers!")

def ttt(p1, p2):
    printer()
    turn = 0
    while True:
        cont = p1("X") if turn % 2 == 0 else p2("O")
        turn += 1
        if cont:
            break
players = {"easy": easy, "user": user, "medium": medium, "hard": hard}
def command():
    global game
    while True:
        try:
            game = [[a[i] for i in range(3)], [a[i] for i in range(3, 6)], [a[i] for i in range(6, 9)]]
            cmd = input("Input command:")
            if cmd == "exit":
                return False
            else:
                c, m, d = cmd.split()
                if c == "start" and m in players and d in players:
                    ttt(players[m], players[d])
                else:
                    raise Exception
        except ValueError:
            print("Bad parameters!")
            continue
command()
