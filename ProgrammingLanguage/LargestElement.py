# nums=[1,24,6,7,34,54,5345]
# max=nums[0]
# for i in range(len(nums)):
#     if nums[i]>max:
#         max=nums[i]
# print(max)

    


nums=[55,32,97,-55,45,32]

# largest=float('-inf')
# secondLargest=float('-inf')
# for i in range(len(nums)):
#     if nums[i]>largest:
#         largest=nums[i]
    
# for i in range(len(nums)):
#     if nums[i]>secondLargest and nums[i]<largest:
#         secondLargest=nums[i]

# print(secondLargest)

# nums.sort()
# print(nums[-2])

# largest=float('-inf')
# secondLargest=float('-inf')
# for i in range(len(nums)):
#     if nums[i]>largest:
#         secondLargest=largest
#         largest=nums[i]
#     elif nums[i]>secondLargest and nums[i]!=largest:
#         secondLargest=nums[i]
# print(secondLargest)




def Check(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
    




