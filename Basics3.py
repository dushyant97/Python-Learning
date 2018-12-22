# looking at loops again (nested loops)

for i in range(1, 51):
    if (i % 3 == 0 and i % 5 == 0):
        print("num", i, "is divisible by both 3 and 5")
    else:
        if (i % 5 == 0):
            print("num", i, "is divisible by 5")
        else:
            if (i % 3 == 0):
                print("num", i, "is divisible by 3")


# Drawing plot

import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[1,2,3,4]
plt.ylabel("Y -axis")
plt.xlabel("x-axis")
plt.plot(x)
plt.show()

from statistics import mean
list=[27,26,45,61,56]
print(mean(list))
