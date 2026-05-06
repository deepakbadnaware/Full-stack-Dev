def BinarySearch(list,target):
    start=0
    end=len(list)-1
    while start<=end:
        mid=start+(end-start)//2
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return start


list=[1,2,3,4,5,6]
target=5

print(BinarySearch(list,target))