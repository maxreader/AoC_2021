import numpy as np

# check to see if element board(x,y) caused a win


def check_board(board, y, x):
    # Column
    if np.all(board[y, :] == 0) or np.all(board[:, x] == 0):
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

to_delete = []
final_call = 0
for call in calls:
    locations = np.nonzero(boards == call)
    boards = np.where(boards == call, False, boards)
    for i, board_num in enumerate(locations[0]):
        board = boards[board_num]
        if check_board(board, locations[1][i], locations[2][i]):
            if len(boards) == 1:
                board_pick = boards[0]
                final_call = call
                break
            to_delete.append(int(locations[0][i]))
    if final_call:
        break
    boards = np.delete(boards, to_delete, 0)
    to_delete = []

print(board_pick)
print(final_call)
print(np.sum(board_pick)*final_call)
