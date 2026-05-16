# def factorial(n):
#     if n==0 or n==1:
#         return 1
    
#     return n*factorial(n-1)


# print(factorial(5))

#1-n

# def printNumber(n):
#     if n==0:
#         return
    
#     print(n)
#     printNumber(n-1)

# printNumber(10)

# def num(i,n):
#     if i>n:
#         return
#     print(i)
#     num(i+1,n)

# num(1,10)


# def sumofn(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     sumofn(sum+i,i+1,n)

# sumofn(0,1,10)

    
    

# def func(n):
#     if n==0:
#         return 1
#     return n*func(n-1)

# print(func(1))


# def reverseArray(nums,start,end):
#     if start>end:
#         return nums
#     nums[start],nums[end]=nums[end],nums[start]
#     return reverseArray(nums,start+1,end-1)

# nums=[5,7,3,2,6,1,5,9]
# print(reverseArray(nums,0,7))


# def isPalindrome(s):
#     start=0
#     end=len(s)-1    
#     while start<end:
#         if s[start]!=s[end]:
#             return False
#         else:
#             start+=1
#             end-=1
#     return True


# s="nitin"

# print(isPalindrome(s))



def isPelin(s,start,end):
    
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    
    return isPelin(s,start+1,end-1)



s="niti"
print(isPelin(s,0,len(s)-1))
    
    