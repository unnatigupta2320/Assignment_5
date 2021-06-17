from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np



#creating x,y for 3D plotting
xx, yy = np.meshgrid([-10,10], range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


#defining planes:  n.T * x = c 
n1 = np.array([3,5,-6]).reshape((3,1))
c1 = 7

#corresponding z for planes
z1 = (c1-n1[0]*xx-n1[1]*yy)/(n1[2])

#plotting planes
Plane=ax.plot_surface(xx, yy, z1,label="Plane", color='g',alpha=0.5)
Plane._facecolors2d=Plane._facecolors3d
Plane._edgecolors2d=Plane._edgecolors3d

#show plot
plt.xlabel('$x-axis$');plt.ylabel('$y-axis$')
plt.legend(loc='best');plt.grid()
