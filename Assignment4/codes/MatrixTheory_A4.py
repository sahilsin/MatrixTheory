import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-0.5,0.5,len)

#Generating points on a parabola
def parab_gen(y,a):
	x = y**2/a
	return x

#parabola parameters
V = np.array(([144,-60],[-60,25]))
u = np.array(([619/2,-136]))
f = 663
#p = np.array(([-3/5,4/5]))

O = np.array(([0,0]))
#Generating the Standard parabola

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
#print(D_vec)
#print(D)
#print(P)
p = P[:,1]
eta = u@p
foc = 2*eta/D_vec[0]
#print(p,foc,D_vec[0])
x = parab_gen(y,foc)

cA = np.vstack((u+eta*p,V))
cb = np.vstack((-f,(eta*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()

print(c,-29/13,-2/13,foc)
plt.plot(-1503/676,-23/169)
plt.annotate("F",(-1503/676,-23/169))
#print(cA,cb)
#print(p,c)

xStandardparab = np.vstack((x,y))
xActualparab = P@xStandardparab + c[:,np.newaxis]

#Labeling the coordinates
parab_coords = np.vstack((O,c)).T
plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['$O$','$c$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(6,0), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.plot(xActualparab[0,:],xActualparab[1,:],label='Parabola',color='r')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()