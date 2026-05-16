nums=[5,1,2,3,4,6,79,8,2,1]


for i in range(len(nums)-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)