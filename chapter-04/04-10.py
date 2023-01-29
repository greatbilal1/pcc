nums = list(range(1, 11))

for num in nums[:3]:
    print(num)

print(nums[:3])

k = 3

strt_idx = (len(nums) // 2) - (k // 2)
end_idx = (len(nums) // 2) + (k // 2)

print(len(nums))
print(strt_idx)
print(end_idx)

print(nums[strt_idx : end_idx + 1])
