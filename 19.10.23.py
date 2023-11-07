nums = [11,2 , 7, 15]
target = 9
newlist = []

for i in range(1, len(nums)):
    if nums[i-1] + nums[i] == target:
        newlist.append(i-1)
        newlist.append(i)

print(newlist)
