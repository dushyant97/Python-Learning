def bubble_sort():
    a=[]
    x=True
    while x:
        a.append (int (input ("Enter number to be entered in the list")))
        print("Enter more number ? 'Y' for yes or 'N' for no")
        temp=input()
        if temp == 'Y' or temp =='y' :
            x=True
        elif temp == 'N' or 'n':
            x=False
    print("List before swapping :")
    print(a)
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print ("List after swapping :")
    print (a)

def selection_sort():
    a = []
    x = True
    while True:
        if x:
            a.append (int (input ("Enter number to be entered in the list")))
            print ("Enter more number ? 'Y' for yes or 'N' for no")
            temp = input ()
            if temp == 'Y' or temp == 'y':
                x = True
            elif temp == 'N' or 'n':
                x = False
        elif x == False:
            break
    print ("List before swapping :")
    print (a)
    for i in range (0, len (a) - 1):
        minimum_index=i
        for j in range (i+1, len (a)):
            if a[j] < a[minimum_index]:
                temp = a[j]
                a[j] = a[minimum_index]
                a[minimum_index] = temp
    print ("List after swapping :")
    print (a)

def insertion_sort():
    a = []
    x = True
    while True:
        if x:
            a.append (int (input ("Enter number to be entered in the list")))
            print ("Enter more number ? 'Y' for yes or 'N' for no")
            temp = input ()
            if temp == 'Y' or temp == 'y':
                x = True
            elif temp == 'N' or 'n':
                x = False
        elif x == False:
            break
    print ("List before swapping :")
    print (a)
    for i in range (1, len (a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    print ("List after swapping :")
    print (a)
