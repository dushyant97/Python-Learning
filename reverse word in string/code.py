def convert(str):
    a = str.split(" ")

    temp =[]
    for i in range(len(a)-1,-1,-1):
        temp.append(a[i])
    
    c= " ".join(temp)
    return c

a=input("Enter the string")
str = convert(a)
print(str)
