score = int(input())
thresholds = {90: "A", 80: "B", 70: "C", 60: "D"}
if score < 60:
    print("F")
else:
    for th in list(thresholds.keys()):
        if score >= th:
            print(thresholds[th])
            break
