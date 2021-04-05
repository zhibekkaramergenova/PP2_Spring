a=[int(i) for i in input().split()]
min=35345
for i in range(len(a)):
    if a[i]>0 and min>a[i]:
        min=a[i]
print(min)    
