raw_input = input()
nums = raw_input.split(" ")
diff = int(nums[1]) - int(nums[0])
print(diff * -1 if diff < 0 else diff)
