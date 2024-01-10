n = int(input())
if n == 0:
    print(0)
else:
    result = n
    i = n - 1
    while i > 0:
        result *= i
        i -= 1
    result = str(result)
    cnt = 0
    j = len(result) - 1
    while j >= 0 and result[j] == '0':
        cnt += 1
        j -= 1
    print(cnt)
