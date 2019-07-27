def fun(temp, k):
    temp.sort()
    print(temp)
    x = set(temp)
    dict = {}
    for i in x:
        dict[i] = temp.count(i)
    for i,j in dict.items():
        if(j == k):
            print(i)

k=3
temp = [9,8,5,1,2,6,5,4,7,8,9,5,6,4,5,9]
a = fun(temp, k)

