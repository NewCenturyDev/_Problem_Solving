import math

# Initalize
K, N = tuple(map(lambda x: int(x), input().split(" ")))
cable_lengths = []
for i in range(K):
    cable_lengths.append(int(input()))
max_length_per_cable = math.floor(sum(cable_lengths) / K)
min_length_per_cable = 1
mid_length_per_cable = math.floor((min_length_per_cable + max_length_per_cable)/2)

# Try with maximum length and reduce one by one
while min_length_per_cable != mid_length_per_cable and mid_length_per_cable != max_length_per_cable:
    cable_cnt = 0
    for cable_length in cable_lengths:
        cable_cnt += math.floor(cable_length / mid_length_per_cable)
    if cable_cnt >= N:
        min_length_per_cable = mid_length_per_cable
    else:
        max_length_per_cable = mid_length_per_cable
    mid_length_per_cable = math.floor((min_length_per_cable + max_length_per_cable) / 2)
if max_length_per_cable == min_length_per_cable:
    print(mid_length_per_cable)
else:
    cable_cnt = 0
    for cable_length in cable_lengths:
        cable_cnt += math.floor(cable_length / max_length_per_cable)
    print(max_length_per_cable if cable_cnt >= N else min_length_per_cable)
