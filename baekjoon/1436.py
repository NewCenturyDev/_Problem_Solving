import math

N = int(input())
output = []


def main():
    for i in range(0, 27):
        for j in range(0, 66):
            handle_10_1(i, j)
        if i % 10 == 6:
            for j in range(0, 1000):
                output.append(int("{}66{:03d}".format(i, j)))
        else:
            for j in range(0, 100):
                output.append(int("{}666{:02d}".format(i, j)))
        for j in range(67, 100):
            handle_10_1(i, j)


def handle_10_1(i, j):
    if j % 10 == 6:
        for k in range(0, 10):
            output.append(int("{}{}666{}".format(i, math.floor(j / 10), k)))
    else:
        output.append(int("{}{:02d}666".format(i, j)))


def get_666(ten_digits):
    bound = "6"
    for _ in range(ten_digits):
        bound += "6"
    return int(bound)


main()
print(output[N - 1])
