import matplotlib.pyplot as plt
import numpy as np

Y= np.linspace(-10,10,100)
X=13*pow(Y,2)

plt.plot(X, Y, '-b')

plt.xlabel('X=(5x-12y+13)/13', color='b')
plt.ylabel('Y=(12x-5y+26)/13', color='g')


plt.title('Parabola')
plt.axhline()
plt.axvline()

plt.grid()
plt.show()