def function(nums,left,right):


    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    
    return nums


nums=[1,2,3,4,5,6,7]
k=3
n=len(nums)

function(nums,n-k,n-1)
function(nums,0,n-k-1)
print(function(nums,0,n-1))