def fun(freq, temp):
    # create a frequency list which indicates if a character has occured in all 2 strings or not
    for i in range(len(temp)):
        str = temp[i]
        for j in range(len(str)):
            freq[i][ord(str[j]) - ord('a')]+=1
    #find minimum occurence of each alphabet which is common in all string
    c=[]
    for i in range(26):
        low=[]
        for j in range(len(freq)):
            low.append(freq[j][i])
        c.append(min(low))
    #printing all those character with descending sort
    alpha=[]
    for i in range(26):
        if c[i]>0:
            alpha.append(chr(i+ord('a')))
    alpha.sort(reverse=True)

    return alpha


temp=['loo','lol','olive']
freq = [[0 for j in range(26)] for i in range(len(temp))]
a = fun(freq, temp)
print(a)
