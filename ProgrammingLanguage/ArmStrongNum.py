import math
num=163
n=num
sum=0
size = int((math.log10(num))+1)
while (n>0):
    lst=n%10
    sum+=pow(lst,size)
    n//=10

if num==sum:
    print("Yes, It is armstrong number")
else:
    print("No, It is not armstrong number")