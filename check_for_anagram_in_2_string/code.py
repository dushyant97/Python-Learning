def anagram(a,b):
    a=sorted(a)
    b=sorted(b)
    if(a == b):
        print("yes")
        print(a,b)
    else:
        print("no")

a=input("Enter the str1 \n")
b=input("Enter the str2 \n")
