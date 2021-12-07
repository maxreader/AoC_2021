import numpy as np

# check to see if element board(x,y) has caused a win


def check_board(board, y, x):
    # Column
    if np.all(board[y, :] == 0) or np.all(board[:, x] == 0):
        return True
    # if x == y or y - x = 4, check diagonal
    elif (x == y or (x+y) == 4):
        d1 = np.all(board.diagonal() == 0)
        d2 = np.all(np.fliplr(board).diagonal() == 0)
        if d1 or d2:
            return True
    else:
        return False


input = open("day_4_input.txt", "r")
calls = [int(x) for x in input.readline().split(",")]
input.readline()
boards = []
i = 0
newBoard = [[]*5]*5
line = input.readline()
while line != "":
    if line == "\n":
        boards.append(newBoard)
        newBoard = [[]*5]*5
        i = 0
        line = input.readline()
    else:
        newBoard[i] = [int(x) for x in line.split()]
        i += 1
        line = input.readline()
boards = np.array(boards)

board_pick = None
final_call = 0
for call in calls:
    if final_call != 0:
        break
    locations = np.nonzero(boards == call)
    boards = np.where(boards == call, False, boards)
    for i, board_num in enumerate(locations[0]):
        board = boards[board_num]
        if check_board(board, locations[1][i], locations[2][i]):
            board_pick = board
            flag = True
            final_call = call
            break
print(board_pick)
print(final_call)
print(np.sum(board_pick, where=board_pick > 0)*final_call)
