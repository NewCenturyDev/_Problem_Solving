n = int(input())
for i in range(n):
    stars = ""
    for j in range(n - (i + 1)):
        stars += " "
    for k in range(i + 1):
        stars += "*"
    print(stars)
