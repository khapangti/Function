def max(num):
    i=0
    max=0
    while i<len(num):
        if num[i]>max:
            max=num[i]
        i=i+1
    return max
print(max([3,5,7,34,2,89,2,5]))