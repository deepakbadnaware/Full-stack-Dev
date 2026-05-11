#Input
num=5674

#Storing num in n for -> without changing input
n=num
ans=0
while (n>0):
    last_digit=n%10
    n//=10
    ans=ans*10+last_digit
print(ans)