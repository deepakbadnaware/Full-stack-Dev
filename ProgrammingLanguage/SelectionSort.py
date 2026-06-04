"""Selection Sort
Time Complexity

Best Case: O(n²)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity: O(1) - sorts in-place

Selection sort has a consistent O(n²) time complexity regardless of the input because it always performs the same number of comparisons: even if the array is already sorted, it still checks every remaining element to find the minimum."""
"""
aapne pass ek array hai usme pele toh ek i index rahega or ek minimum index raheaga starting me i rahega phir ek j rahega jo i +1 se chalega 
yaha hum check karenge ki kabhi apna nums[j] < raha toh nums[miniindex se] toh aapan ko miniindx ko j bana dena phir jo chota value aaye usko swap kar dena hai i se means first element se 
"""

# accending order 
nums =[5,2,6,3,4,5,6,4,1]
for i in range(len(nums)):
    midx=i
    for j in range(i+1,len(nums)):
        if nums[j]<nums[midx]:
            midx=j
    nums[i],nums[midx]=nums[midx],nums[i]
print(nums)
