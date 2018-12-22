"""
def m():
    a=[["dog","cat"," ","sheep"," "],["lion"," ","hippo"," ","eagle"]]
    for i in a:
        while(" " in i):
            if " " in i:
                x=i.index(" ")
                i.__delitem__(x)
                i.insert(x,"hello")
    print(a)

def n():
    a="hello"
    b=tuple(a)
    c,d,e,f,g=b
    print(c)
    print(d)
    h=set(b)

def  o():
    animal=["DOG","CAT"]
    number=[100,50]
    for index,value in enumerate(animal):
        print(value,number[index])

a={"Dollar":50,
   "Euro":70,
   "Diram":20}
for i in a.items():
    print(i)
    print(type(i))

total = 10
def add_to_total(a):
   global total
    total = total + a
add_to_total(20)

print(total)
a=tuple('python')
b=(a[::3])
print(len(b))

i=50
j="Hello"
print("First argument: {i}, second one: {j}".format(i="Hului",j=100) )
print("First arg is %s and second is %d"%("Hululullu",i))

b = {"Dollar": 50,
     "Euro": 70,
     "Pound": 80}
for i in b:
    temp = "The value of " + i + " is {" + i + "}"
    print (temp.format (**b))

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
"""

a=[1,3,8,5,3,2]
a.sort()
b=sorted(a)