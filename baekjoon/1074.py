Z, R, C = tuple(map(lambda x: int(x), input().split(" ")))

# 각 구역의 시작수. 쪼개는 횟수에 따라 누적됨.
base_sum = 0


def find_quadrant(current_z, current_r, current_c, current_sum):
    width = 2 ** current_z
    height = 2 ** current_z
    if current_c < width / 2 and current_r < height / 2:
        current_sum += 0
    elif current_c >= width / 2 and current_r < height / 2:
        current_c -= width / 2
        current_sum += 1 * (width / 2) * (height / 2)
    elif current_c < width / 2 and current_r >= height / 2:
        current_r -= height / 2
        current_sum += 2 * (width / 2) * (height / 2)
    elif current_c >= width / 2 and current_r >= height / 2:
        current_c -= width / 2
        current_r -= height / 2
        current_sum += 3 * (width / 2) * (height / 2)
    else:
        print("ERROR")

    # If sub section is exist(current Z > 1, run find_quadrant for target section)
    if current_z > 1:
        return find_quadrant(current_z - 1, int(current_r), int(current_c), int(current_sum))
    else:
        return int(current_sum)


print(find_quadrant(Z, R, C, base_sum))
