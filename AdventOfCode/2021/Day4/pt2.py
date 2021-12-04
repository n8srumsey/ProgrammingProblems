# Day4 Part 2 

data_input = "./input.txt"

with open(data_input) as f:
    data = [l.rstrip('\n') for l in f.readlines()]

def count_boards():
    count = 0
    for l in data:
        if l == '':
            count += 1
    return count

def gen_boards():
    boards = []
    board_data = data[2:]
    for i in range(count_boards()):
        boards.append([])
        for j in range(5):
            squares = board_data[i*6 + j].split()
            row = []
            for s in squares:
                row.append([int(s), False])
            boards[i].append(row)
    return boards

def print_board(b):
    for r in b:
        print(r)
    print()

def get_draws():
    return [int(d) for d in data[0].split(',')]

def update_boards(boards, drawn_num):
    for b in boards:
        for r in b:
            for c in r:
                if c[0] == drawn_num:
                    c[1] = True
    return boards

def check_win(boards):
    win = False
    has_won = []
    winning_boards = []
    for i, b in enumerate(boards):
        this_win = False
        for r in b:
            if r[0][1] and r[1][1] and r[2][1] and r[3][1] and r[4][1]:
                this_win = True
                win = True
                has_won.append(i)
                winning_boards.append(b)
                break
        for c in range(5):
            if b[0][c][1] and b[1][c][1] and b[2][c][1] and b[3][c][1] and b[4][c][1] and not this_win:
                win = True
                has_won.append(i)
                winning_boards.append(b)
                break
    return win, has_won, winning_boards

def calc_sum_unmarked(board):
    sum = 0
    for r in board:
        for c in r:
            if not c[1]:
                sum += c[0]
    return sum

if __name__=='__main__':
    n_boards = count_boards()
    boards = gen_boards()
    draws = get_draws()
    won = []
    prev_won = []
    for draw in draws:
        prev_won = won
        boards = update_boards(boards, draw)
        win, won, winning_boards = check_win(boards)
        winning_board = [b for b in won if b not in prev_won]
        if len(won) == n_boards:
            unmarked = calc_sum_unmarked(boards[winning_board[0]])
            print(unmarked, draw, unmarked * draw)
            break
            