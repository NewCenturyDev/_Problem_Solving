raw_input = input()
nums = list(map(lambda n: int(n)**2, raw_input.split()))
print(sum(nums) % 10)
