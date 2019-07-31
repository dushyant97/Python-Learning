a=[3,8,8,5,4,4,4,9,9,9,9,9,9]
b=list(set(sorted(a)))

dict={}
for i in b:
    dict[i]=a.count(i)
b=sorted(dict.items(), key=lambda x : x[1])

x=[]
for i in b:
    for j in range(i[1]):
        x.append(i[0])
print("Unsorted List", a)
print("Sorted List", x)
