# Using print statement
print("Hello World")
a = "Haku-Nama-Tata"
print(a)
print("Timon and Pumba says", a)
# taking input from user
print("Enter your name")
a = input()
print("Hello", a)
# note- input is taken as string , so for any airthamatic calculations we typecast it to int
a1 = int(input("Enter any number"))
a1 = a1 * 2
print(a1)
# use semi-colon when you want to use multiple statement in a single line
# LOOPS- if
a = int(input("Enter your choice"))
if (a == 1):
    print("1 was entered")
if (a == 2):
    print("2 was entered")

# LOOPS- for ,, i will move form 0 ,1 ,2

for i in range(3):
    print("HELLO")

# LOOPS- while
n = 1
while (n == 1):
    print("Aye Aye!!")
    n = int(input("Enter value of n"))
