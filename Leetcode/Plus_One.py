def plus_one(digits):
    length=len(digits)-1
    for i in range(length,-1,-1):
        if digits[i]+1!=10:
            digits[i]+=1
            return digits
        digits[i]=0
        if i==0:
            return [1]+digits
        
print(plus_one([9]))

