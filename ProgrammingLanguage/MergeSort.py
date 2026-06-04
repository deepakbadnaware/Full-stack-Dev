

def merge(left,right):
    result=[]
    i=0
    j=0
    n=len(left)
    m=len(right)

    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1    
    while i<n:
        result.append(left[i])
        i+=1
    while j<m:
        result.append(right[j])
        j+=1
    return result

def merge_Sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2

    left_arr=arr[:mid]
    right_arr=arr[mid:]

    left=merge_Sort(left_arr)
    right=merge_Sort(right_arr)

    return merge(left,right)




arr=[6,52,67,321,1,1,4,2]
print(merge_Sort(arr))