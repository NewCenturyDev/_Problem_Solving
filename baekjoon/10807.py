import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
target = int(sys.stdin.readline().rstrip())

cnt = 0
for n in nums:
    if n == target:
        cnt += 1
print(cnt)
