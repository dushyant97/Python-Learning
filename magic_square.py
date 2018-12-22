'''Basic facts of Magic Square:
1. Magic Number is n(n^2+1)/2
2. position of 1 is always (n/2,n-1)=(p,q)
3. position of 2 is always (p-1,q+1), if row becomes -1 then change it to n-1 or if column becomes n then change it to 0
4. if calculated position has already a number, then decrease the column position by 2 and increment row by 1
5. if anytime row and column becomes (-1,n) then change it to  (0,n-2)
'''


def magic_square(n):
    magic_sqr = []  # creating matrix
    for i in range (n):
        l = []
        for j in range (n):
            l.append (0)
        magic_sqr.append (l)

    i = n // 2  # // means dividing and converting it int at floor value
    j = n - 1
    num = n * n
    count = 1

    while (count <= num):
        if (i == -1 and j == n):  # condition 4
            i = 0
            j = n - 2
        else:
            if (j == n):  # condition 2
                j = 0

            if (i < 0):
                i = n - 1

        if (magic_sqr[i][j] != 0):
            j = j - 2
            i = i + 1
            continue
        else:
            magic_sqr[i][j] = count
            count = count + 1
        i = i - 1
        j = j + 1

    for i in range (n):
        for j in range (n):
            print (magic_sqr[i][j], end=" ")
        print ()


print ("Enter how size for magic square")
n = int (input ())
magic_square (n)
