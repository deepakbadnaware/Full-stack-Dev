nums=[5,6,7,7,1,9,11,1,1,5,1,1]

freq={}
# for i in range(len(nums)):
#     if nums[i] not in freq:
#         freq[nums[i]]=1
#     else:
#         freq[nums[i]]+=1
# print(freq)


for i in range(len(nums)):
    freq[nums[i]]=freq.get(nums[i],0)+1

print(freq)

