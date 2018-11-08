import copy
import time


def solve(bd):
    num = 81
    optimalVariant = [9, 0, 0]
    optValues = []
    for i in range(len(bd)):
        for j in range(len(bd[i])):
            if bd[i][j] == 0:
                values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for k in range(9):
                    if not bd[i][k] == 0:
                        if bd[i][k] in values:
                            values.remove(bd[i][k])
                    if not bd[k][j] == 0:
                        if bd[k][j] in values:
                            values.remove(bd[k][j])
                for p in range((i // 3) * 3, ((i // 3) * 3) + 3):
                    for r in range((j // 3) * 3, ((j // 3) * 3) + 3):
                        if bd[p][r] in values:
                            values.remove(bd[p][r])
                if len(values) < optimalVariant[0]:
                    optimalVariant = [len(values), i, j]
                    optValues = copy.deepcopy(values)
            else:
                num -= 1
    if num > 0:
        while not len(optValues) == 0:
            bd[optimalVariant[1]][optimalVariant[2]] = optValues[0]
            if solve(bd) == True:
                return True
            bd[optimalVariant[1]][optimalVariant[2]] = 0
            optValues.pop(0)
    else:
        return True
    return False


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()
    print()


def main():
    start_time = time.time()
    board = [[0 for x in range(9)] for x in range(9)]
    with open('task.txt', 'r') as f:
        for i in range(9):
            for j in range(9):
                board[i][j] = f.read(1)
                if board[i][j] == ".":
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
    printBoard(board)
    solve(board)
    printBoard(board)
    print("--- %s seconds ---" % (time.time() - start_time))


main()