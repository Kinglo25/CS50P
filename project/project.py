import random

ROW = 3
COL = 3
X = ['x', 'x', 'x']
O = ['o', 'o', 'o']

def main():
    board = [['-']*ROW for _ in range(COL)]
    start_game(board)
    display_board(board)

def filled(b):
    for row in b:
        for case in row:
            if case == '-':
                return False
    return True

def player_has_won(b):
    #check rows
    for row in b:
        if row in (X, O):
            return True
    #check cols
    tmp_lst = []
    for y in range(COL):
        tmp_lst.clear()
        for x in range(ROW):
            tmp_lst.append(b[y][x])
            if (tmp_lst in (X, O)):
                return True
    #check diag \:
    tmp_lst.clear()
    for x, y in zip(range(ROW), range(COL)):
        tmp_lst.append(b[y][x])
    if (tmp_lst in (X, O)):
        return True
    #check diag /:
    tmp_lst.clear()
    for x, y in zip(reversed(range(ROW)), range(COL)):
        tmp_lst.append(b[y][x])
    if (tmp_lst in (X, O)):
        return True
    return False

def display_board(b):
    print("\n    1    2    3")
    for i, row in zip(range(1, 4), b):
        print(f"{i} {row}")
    print("")

def start_game(b):
    #randomly chose who begins
    if turn := random.randint(0, 1):
        print("Computer begins with the 'x'!")
    else:
        print("You begin with the 'o'!")
    #loop until winner or draw
    while True:
        display_board(b)
        #turn == 1 when computer as to play
        if turn:
            #loop for a case not already used
            while True:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if already_used(b, x, y):
                    continue
                break
            #update the case
            b[x][y] = 'x'
            print("The computer played!")
        else:
             #turn == 0 when player as to play
            print("Your turn!")
            while True:
                #loop for a case not already used then update that case
                try:
                    x = int(input("Choose a row: ")) - 1
                    y = int(input("Choose a column: ")) - 1
                    if x < 0 or x > 2 or y < 0 or y > 2:
                        raise IndexError
                except (ValueError, IndexError):
                    print("Chose a value between 1 and 3 (both included)")
                    continue
                else:
                    if already_used(b, x, y):
                        print("Already used")
                        continue
                    break
            #update the case
            b[x][y] = 'o'
            print("You played!")
        if player_has_won(b):
            if turn:
                print("The computer won! Game over")
            else:
                print("You won! Ggwp")
            break
        if filled(b):
            print("The board is filled, this is a draw!")
            break
        #update who's turn it is
        turn = not turn

def already_used(b, x, y):
    if b[x][y] in ('o', 'x'):
        return True
    return False

if __name__ == "__main__":
    main()