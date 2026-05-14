nums=[5,6,7,7,1,9,11,1,1,5,1,1]
freq={}
for i in nums:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1

for i in nums:
    freq[i]=freq.get(i,0)+1

print(freq)
