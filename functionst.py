def num(list):
    i=0
    while i<len(list):
        list.sort()
        i=i+1
    return list
print(num([6,8,4,3,9,56,0,34,7,15]))