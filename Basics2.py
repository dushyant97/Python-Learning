#intro to list

songs=["Backstreet Boys","Akon","Eminem","Enrique","Akon"]
print(songs)

#using loops in list

for i in songs:
    print(i)

#OR

for i in range(4):
    print(songs[i])

#printing specific portion

print("Second song is",songs[1])

#operations on list
#append

songs.append("Selena Gomez")
print(songs)

#for mathematical values, dont use ""

a=[10,22,1,6,3,87,9,100,222]
print(a)
#sort --> sorts the list  // used for only mathematical operation

a.sort()
print(a)

#reverse -- > reverses the list // if reversed again we will get the same list

a.reverse()
print(a)

# SLICING  --> gives sublist  // format->  name=[start-index:last-index + 1]


name=["tyagi","uppal","pinky","gupta","dushyant"]
print(name)
print(name[1:3]) #OR
name1=name[1:3]
print(name1)

#if no values are provided, complete list appears

print(name[:])

#if no end value- then we get the list till the end

print(name[1:])

#if no start value-- then it starts from starting of list to the gioven value

print(name[:3])

