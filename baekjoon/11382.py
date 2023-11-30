raw_input = input()
nums = raw_input.split(" ")
print(sum(list(map(lambda n: int(n), nums))))
