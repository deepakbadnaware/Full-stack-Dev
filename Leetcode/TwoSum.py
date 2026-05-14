nums=[2,7,11,15,16]
target=26
seen=dict()

for i in range(len(nums)):
    num=nums[i]
    total=target-num
    if total in seen:
        print(seen[total],i)
    seen[num]=i

