import sys

submitted = [0]
for i in range(30):
    submitted.append(0)
for i in range(28):
    submitted[int(sys.stdin.readline().rstrip())] = 1
for i in range(30):
    if submitted[i + 1] == 0:
        print(i + 1)
