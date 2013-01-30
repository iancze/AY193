import asciitable
import matplotlib.pyplot as plt

#Reading in data
data = asciitable.read("ps_1_data_set.txt")
xi = data["x_i"]
yi = data["y_i"]

#Simple way
plt.plot(xi,yi,".")

#Label your axes!
plt.xlabel("x")
plt.ylabel("y")

#Set the title
plt.title("Data Set 1")

#Save the figure
plt.savefig("basic_plot.eps")


