N = int(input())
commands = []
job_stack = []
last_time_elapsed = 0
for i in range(N):
    command, character, time = input().split(" ")
    # commands.append({
    #     'command': command,
    #     'character': character,
    #     'time': int(time),
    # })
    last_time_elapsed = int(time)
    if command == "type":
        job_stack.append((int(time), character))
    if command == "undo":
        removed_char = ""
        reset_point = last_time_elapsed - int(character)
        undo_job_list = []
        for job in job_stack:
            if job[0] >= reset_point:
                undo_job_list.append(job)
        for j in range(len(undo_job_list) - 1, -1, -1):
            if undo_job_list[j][1] == "":
                continue
            elif undo_job_list[j][1][0] == "-":
                removed_char += undo_job_list[j][1].replace("-", "")
            else:
                removed_char += "-"
                removed_char += undo_job_list[j][1]
        job_stack.append((int(time), removed_char))

answer = ""
will_pass_next = False
# for job in job_stack[:(last_time_elapsed + 1)]:
for job in job_stack:
    for k in range(len(job[1])):
        if will_pass_next:
            will_pass_next = False
        elif job[1][k] == "-":
            remove_char = job[1][k + 1]
            answer = answer.replace(remove_char, "")
            will_pass_next = True
        else:
            answer += job[1][k]
print(answer)
