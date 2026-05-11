num = 121
n = num
reversed_num = 0

# Reverse the number by extracting digits
while n > 0:
    last_digit = n % 10
    n //= 10
    reversed_num = reversed_num * 10 + last_digit

# Check if original equals reversed
if num == reversed_num:
    print("Yes, it is a Palindrome number")
else:
    print("No, it is not a Palindrome number")