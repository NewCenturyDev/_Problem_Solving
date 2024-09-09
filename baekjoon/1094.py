X = int(input())
sticks = [64]
continue_flag = True


# 일단 이렇게 풀면 시뮬레이션 방식으로 푸는건데, 왠지 2진수 원리로다가 1갯수 세리는걸로 풀어도 될거같다.
def do_process():
    global sticks
    global continue_flag
    stick_length_sum = sum(sticks)
    if stick_length_sum > X:
        sum_stick_length = sum(sticks)
        shortest_stick_len = min(sticks)
        for i in range(len(sticks)):
            if sticks[i] == shortest_stick_len:
                sticks[i] = int(sticks[i] / 2)
                if sum_stick_length - sticks[i] == X:
                    continue_flag = False
                    break
                elif sum_stick_length - sticks[i] > X:
                    break
                else:
                    sticks.append(sticks[i])
                    break
    elif stick_length_sum == X:
        continue_flag = False


while continue_flag:
    do_process()
print(len(sticks))


# 이렇게.
print(str(bin(X))[2:].count('1'))
