import asciitable
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


#Read in data
data = asciitable.read("ps_1_data_set.txt")
xi = data["x_i"]
yi = data["y_i"]

sigma = 0.08

def model(x,a,b):
    return a + b * x

@np.vectorize
def chi_sq(a,b,sigma):
    return np.sum(((yi - model(xi,a,b))/sigma)**2)

A = np.arange(0., 1., 0.01)
B = np.arange(-0.4, 1.1, 0.01)
A_grid, B_grid = np.meshgrid(A, B)

#chi_func = lambda a, b: chi_sq(a,b,sigma)
L = np.log10(np.exp(-1.0 * chi_sq(A_grid, B_grid,sigma)/2))

np.save("A",A_grid)
np.save("B",B_grid)
np.save("L",L)

fig = plt.figure()
ax = fig.add_subplot(111)
CS = ax.contour(A_grid,B_grid,L)
ax.clabel(CS, inline=1, fontsize=10,fmt = '%2.0f')
ax.set_xlabel("a")
ax.set_ylabel("b")
#ax.set_zlabel(r"$\log_{10}({\cal L})$",labelpad=20)
#plt.show()
fig.savefig("chi_contour.eps")
