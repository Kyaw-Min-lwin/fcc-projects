nums = [0, 1, 0, 3, 12] # output should be [1, 3, 12, 0, 0]
insert_pos = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[insert_pos] = nums[i]
        insert_pos += 1
print(nums)
# Fill the remaining positions with zeros
for i in range(insert_pos, len(nums)):
    nums[i] = 0

print(nums)

import math
print(-math.inf)