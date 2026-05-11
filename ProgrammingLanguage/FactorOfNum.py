#brute force

# n=20
# ans=[]
# for i in range(1,n+1):
#     if n%i==0:
#         ans.append(i)
# ans.append(n)
# print(ans)


# better code O(n) and O(k) ->number of factorial

# n=20
# ans=[]
# for i in range(1,(n//2)+1):
#     if n%i==0:
#         ans.append(i)
# ans.append(n)
# print(ans)


# optimal Code


from math import sqrt

n=10
ans=[]
for i in range(1,int(sqrt(n))):
    if n%i==0:
        ans.append(i)
        if n%i!=i:
            ans.append(n//i)

ans.sort()
print(ans)



#O(sqrt(n)+ O(n logn))