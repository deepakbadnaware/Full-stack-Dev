

# def markAsInf(nums,row,col):
#     r=len(nums)
#     c=len(nums[0])
#     for i in range(r):
#         if nums[i][col]!=0:
#             nums[i][col]=float('-inf')
#     for j in range(c):
#         if nums[row][j]!=0:
#             nums[row][j]=float('-inf')
    

      
    


# def setZeros(nums):
#     r=len(nums)
#     c=len(nums[0])
#     for i in range(r):
#         for j in range(c):
#             if nums[i][j]==0:
#                 markAsInf(nums,i,j)
     
#     for i in range(r):
#         for j in range(c):
#             if nums[i][j]==float('-inf'):
#                 nums[i][j]=0
#     print(nums)

# nums=[[5,3,1],[5,0,5],[8,9,6]]
# setZeros(nums)



nums=[[5,3,1],[5,0,5],[8,9,6]]

# def mark(nums):
#     r=len(nums)
#     c=len(nums[0])
#     col_track=[0 for _ in range(c)]
#     row_track=[0 for _ in range(r)]
#     for i in range(r):
#         for j in range(c):
#             if nums[i][j]==0:
#                 col_track[j]=-1
#                 row_track[i]=-1
#     for i in range(r):
#         for j in range(c):
#             if row_track[i]==-1 or col_track[j]==-1:
#                 nums[i][j]=0

#     print(nums)
# mark(nums)

r=len(nums)
c=len(nums[0])
result=[0*r for _ in range(c)]

for i in range(r):
    for j in range(c-1,-1,-1):
        result[i][j]=nums[i][j]