def fun(freq, temp):
    # create a frequency list which indicates if a character has occurred in all 2 strings or not
    for i in range(len(temp)):
        str = temp[i]
        for j in range(len(str)):
            freq[i][ord(str[j]) - ord('a')]+=1

    #find the frequency of minimum character required
    c=[]
    for i in range(26):
        low=[]
        for j in range(len(freq)):
            low.append(freq[j][i])
        minimum = min(low)
        diff = [i-minimum for i in low]
        c.append(max(diff))

    total = sum(i for i in c)
    return total


a= input("Enter the first string\n")
b= input("Enter the second string\n")
temp=[a,b]
freq = [[0 for j in range(26)] for i in range(len(temp))]
a = fun(freq, temp)
print(a)
