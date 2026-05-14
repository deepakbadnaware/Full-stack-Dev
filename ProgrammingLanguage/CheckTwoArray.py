n=[5,2,2,3,1,5,5,7,5,10]
m=[10,11,1,9,5,67,2]
"""
preValueInserted
constraints: i<n[i]<=10
n can have 10^8
m can have 10^8
Brute force TC
M*N -> 10^16
"""

n=[5,3,2,2,1,5,5,7,5,10]
m=[10,11,1,9,5,67,2]
# size=len(n)+1
# list=[0]*size
# for nums in n:
#     list[nums]+=1

# for nums in m:
#     if nums<1 or nums>10:
#         print(0)
#     else:
#         print(list[nums])


# freq={}
# # print(n)
# for i in range(len(n)):
#     if n[i] not in freq:
#         freq[n[i]]=1
#     else:
#         freq[n[i]]+=1

# for nums in m:
#     if nums<1 or nums>10:
#         print(0)
#     else:
#         print(freq.get(nums,0))
