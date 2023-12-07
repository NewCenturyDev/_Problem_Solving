import sys
sys.setrecursionlimit(10**7)


def main():
    # Get num of test cases (T)
    t = int(input())
    for i in range(t):
        run_test_case()


def run_test_case():
    # Get width of board (M), height of board(N), num of inputs(K)
    m, n, k = tuple(map(lambda s: int(s), input().split(" ")))
    board = []
    answer = 0

    # Setup board
    setup_board(board, m, n)

    # Setup plant
    setup_plant(board, k)

    # Find plant block and mark 2 by using DFS
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                answer += 1
                check_wasd(board, m, n, x, y)
    print(answer)


def check_wasd(board, m, n, x, y):
    board[y][x] = 2
    if x > 0 and board[y][x - 1] == 1:
        check_wasd(board, m, n, x - 1, y)
    if x < m - 1 and board[y][x + 1] == 1:
        check_wasd(board, m, n, x + 1, y)
    if y > 0 and board[y - 1][x] == 1:
        check_wasd(board, m, n, x, y - 1)
    if y < n - 1 and board[y + 1][x] == 1:
        check_wasd(board, m, n, x, y + 1)


def setup_board(board, m, n):
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        board.append(row)


def setup_plant(board, k):
    for j in range(k):
        pos_x, pos_y = input_target_position()
        board[pos_y][pos_x] = 1


def input_target_position():
    return tuple(map(lambda x: int(x), input().split(" ")))


# Run script
main()
