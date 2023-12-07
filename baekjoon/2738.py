import sys


def main():
    n, m = tuple(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
    a = []
    b = []
    input_matrix(a, n)
    input_matrix(b, n)
    print_sum(a, b, n, m)


def input_matrix(matrix, n):
    for i in range(n):
        matrix.append(list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))))


def print_sum(a, b, n, m):
    for i in range(n):
        for j in range(m):
            end_char = "\n" if j == m - 1 else " "
            print(a[i][j] + b[i][j], end=end_char)


main()
