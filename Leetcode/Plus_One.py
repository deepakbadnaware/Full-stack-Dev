def plus_One(digits):

    last=len(digits)-1
    digits[last]+=1
    if digits[last]==9:
        return [1].append(digits)
    else:
        return digits
    


digits=[9]
print(plus_One(digits))