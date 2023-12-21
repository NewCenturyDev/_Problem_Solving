import math

num = ""
while num != "0":
    num = input()
    if num != "0":
        isPalindrom = True
        limit = math.floor(len(num) / 2)
        for i in range(limit):
            if num[i] != num[-(i + 1)]:
                isPalindrom = False
        print("yes" if isPalindrom else "no")
