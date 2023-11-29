n = int(input())
raw_scores = input().split()
scores = list(map(lambda s: int(s), raw_scores))
max_score = max(scores)
results = []

for score in scores:
    results.append(score / max_score * 100)

print(sum(results)/len(results))
