def num(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return sum
print(num([1,2,3,4,5]))
