import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = tuple(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
    print(a + b)
