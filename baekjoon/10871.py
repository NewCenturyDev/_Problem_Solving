import sys

N, X = tuple(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
nums = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

for i in range(N):
    if nums[i] < X:
        print(nums[i])
