with open("input.txt") as _file:
    nums = []
    for line in _file:
        nums.append(int(line))
    print(nums)

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                num_1 = nums[i]
                num_2 = nums[j]
                num_3 = nums[k]

print(num_1* num_2* num_3)
