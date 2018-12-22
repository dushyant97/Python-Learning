# Bubble sort

def bubble(a):
    n=len(a)

    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

a=[2,1,3]
print("Before sorting ", )
bubble(a)
print(a)


#binary search

def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag =0         #0 value means that the element has not yet been fo

    while(first_pos<=last_pos and flag==0):
        mid=(first_pos+last_pos)//2
        if x==a[mid]:
            flag=1
            print("The element is at mid position",mid)
            return
        else:
            if x<a[mid]:
                last_pos=mid-1
            else:
                first_pos=mid+1
        print("Element not found")

a=[]
for i in range(1,11):
    a.append(i)

binary_search(a,5)
