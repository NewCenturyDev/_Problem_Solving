sorted_idx = 0


def main():
    n = int(input())
    a = list(map(lambda x: int(x), input().split(' ')))
    s = int(input())
    check_and_move(a, n, s)
    result = str(a[0])
    for i in range(1, n, 1):
        result += " "
        result += str(a[i])
    print(result)


def check_and_move(a, n, s):
    global sorted_idx
    if s > 0:
        max_i, max_n = find_max(a, sorted_idx, n if sorted_idx + s >= n else sorted_idx + s + 1)
        if check_max_can_move_with_s(s, max_i - sorted_idx):
            for i in range(max_i, sorted_idx, -1):
                swap(a, i - 1, i)
                s -= 1
            sorted_idx += 1
        if sorted_idx < n:
            check_and_move(a, n, s)


def find_max(a, start_i, end_i):
    max_num = -1
    max_i = start_i
    for i in range(start_i, end_i, 1):
        if max_num < a[i]:
            max_num = a[i]
            max_i = i
    return max_i, max_num


def check_max_can_move_with_s(s, max_i):
    return max_i <= s


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


main()
