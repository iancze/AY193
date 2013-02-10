import asciitable
import matplotlib.pyplot as plt
import numpy as np

#Reading in data
data = asciitable.read("ps_1_data_set.txt")
xi = data["x_i"]
yi = data["y_i"]

fig = plt.figure(figsize=(5,5))
ax1 = plt.subplot2grid((2,2), (0,0), colspan=2)
ax1.plot(xi,yi,".k") #the "." plots data points instead of a line, "k" is black

#Set the title
ax1.set_title("Data Set 1")

xs = np.linspace(-1,1)

def line(x,p):
    return p[0] + p[1] * x

ax1.plot(xs,line(xs,[0.5,0.6]),"g",label="Best guess: a=0.5, b=0.6")
ax1.legend(loc="best",prop={'size':10})
x_m = np.argsort(xi)[25] #determine the median
ax1.errorbar(xi[x_m],yi[x_m],yerr=0.1) #plot the sigma point 
ax1.annotate(r'$\sigma \approx 0.1$',(xi[x_m],yi[x_m]-0.3))

ax2 = plt.subplot2grid((2,2), (1,0))
ax2.plot(xi,yi,".k") #the "." plots data points instead of a line, "k" is black
ax2.plot(xs,line(xs,[0.47,0.6]),"b",label="Low a=0.47")
ax2.plot(xs,line(xs,[0.53,0.6]),"r",label="High a=0.53")
ax2.legend(loc="best",prop={'size':8})
#Label one corner of the axes!
ax2.set_xlabel("x")
ax2.set_ylabel("y")

ax3 = plt.subplot2grid((2,2), (1, 1))
ax3.plot(xi,yi,".k") #the "." plots data points instead of a line, "k" is black
ax3.plot(xs,line(xs,[0.5,0.55]),"b",label="Low b=0.55")
ax3.plot(xs,line(xs,[0.5,0.65]),"r",label="High b=0.65")
ax3.legend(loc="best",prop={'size':8})

for ax in [ax1,ax2,ax3]:
    ax.tick_params(axis='both', labelsize=10)

fig.subplots_adjust(wspace=0.25) #adjust the width between figures

#Save the figure
fig.savefig("basic_plot.eps")
