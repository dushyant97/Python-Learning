def swap():
    a = int (input ("Enter first number"))
    b = int (input ("Enter two number"))
    print ("The two numbers before swapping are: a=", a, " & b=", b)
    a = a + b
    b = a - b
    a = a - b
    print ("The two numbers after swapping are: a=", a, " & b=", b)


def string_reverse():
    a = input ("Enter string")
    temp = " "
    b = len (a)
    b = b - 1
    for i in range (b, -1, -1):  # write down for range
        temp = temp + a[i]
    print (temp)


def palindrome_string():
    a = input ("Enter String")
    temp = ""
    b = len (a) - 1
    for i in range (b, -1, -1):  # write down for range
        temp = temp + a[i]
    if a == temp:
        print ("String is palindrome")
    else:
        print ("String is not palindrome")


def divisor_finder():
    a = int (input ("Enter the number"))
    temp = []
    for i in range (1, a + 1):
        if a % i == 0:
            temp.append (i)
    print ("The divisors of the given number are ", temp)

def largest_no():
    a = True
    b = []
    while a != False:
        a = int (input ("Enter number"))
        b.append (a)
        c = input ("Press 'Y' to continue and 'N' to finish")
        if c == 'Y' or c == 'y':
            a = True
        else:
            a = False
    largest = b[0]
    for i in b:
        if largest < i:
            largest = i
    print ("Largest number is ", largest)



def matrix_add_subtract():
    m = int (input ("Enter number of rows"))
    n = int (input ("Enter number of columns"))
    print ("For Matrix A")
    d = [[int (input ("Enter value for row " + str (j) + " and column " + str (i))) for i in range (n)] for j in
         range (m)]
    print ("For Matrix B")
    e = [[int (input ("Enter value for row " + str (j) + " and column " + str (i))) for i in range (n)] for j in
         range (m)]
    print ("Matrix A is:")
    for i in d:
        print (i)
    print ("Matrix B is:")
    for i in e:
        print (i)
    c = [[0 for i in range (n)] for j in range (m)]
    for i in range (len (d)):
        for j in range (len (d[0])):
            c[i][j] = d[i][j] + e[i][j]
    print ("Matrix C is:")
    for i in c:
        print (i)


def multiply_matrix():
    m = int (input ("Enter number of rows"))
    n = int (input ("Enter number of columns"))
    print ("For Matrix A")
    d = [[int (input ("Enter value for row " + str (j) + " and column " + str (i))) for i in range (n)] for j in
         range (m)]
    print ("For Matrix B")
    e = [[int (input ("Enter value for row " + str (j) + " and column " + str (i))) for i in range (n)] for j in
         range (m)]
    print ("Matrix A is:")
    for i in d:
        print (i)
    print ("Matrix B is:")
    for i in e:
        print (i)
    c = [[0 for i in range (n)] for j in range (m)]
    for i in range (len (d)):  # iterate through rows of first
        for j in range (len (e[0])):  # iterate through column of second
            for k in range (len (e)):  # iterate through rows of second
                c[i][j] = c[i][j] + d[i][k] * e[k][j]
    print ("Matrix C is:")
    for i in c:
        print (i)


def transpose():
    m = int (input ("Enter number of rows"))
    n = int (input ("Enter number of columns"))
    print ("For Matrix A")
    d = [[int (input ("Enter value for row " + str (j) + " and column " + str (i))) for i in range (n)] for j in
         range (m)]
    print ("Given Matrix is:")
    for i in d:
        print (i)
    c = [[0 for i in range (n)] for j in range (m)]
    for i in range (m):
        for j in range (n):
            c[i][j] = d[j][i]
    print ("Transpose Matrix is:")
    for i in c:
        print (i)


def greatest_common_divisor():
    a = int (input ("Enter the first number"))
    b = int (input ("Enter the first number"))
    x = []
    for i in range (2, a + 1):
        if a % i == 0:
            x.append (i)
    y = []
    for i in range (2, b + 1):
        if b % i == 0:
            y.append (i)
    print ("The divisors of the first number are ", x)
    print ("The divisors of the second number are ", y)
    common = []
    for i in x:
        if y.count (i) >= 1:
            common.append (i)
    gcd = max (common)
    print ("The greatest common divisor is ", gcd)


def lcm():
    a = int (input ("Enter the first number"))
    b = int (input ("Enter the first number"))
    i = max (a, b)
    while True:
        if i % a == 0 and i % b == 0:
            lcm = i
            break
        i = i + 1
    print ("The LCM of two numbers is ", lcm)


def hcf():
    a = int (input ("Enter the first number"))
    b = int (input ("Enter the first number"))
    i = min (a, b)
    while True:
        if a % i == 0 and b % i == 0:
            hcf = i
            break
        i = i + 1
    print ("The HCF of two numbers is ", hcf)

# DO ALL SORTING AND  THEN NPTEL AND SHORTEST PALLINDROME and DS
