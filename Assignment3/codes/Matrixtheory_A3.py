import matplotlib.pyplot as plt
import numpy as np


A = 90
x=(180-90)/2

print("Value of angle B and C is",x)

x1=[0,1,0]
y1=[0,0,1]


plt.triplot(x1,y1,color='r')



plt.title('triangle')

plt.grid()
plt.show()