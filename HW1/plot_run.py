import asciitable
import matplotlib.pyplot as plt
import numpy as np

data = asciitable.read("runa.dat")
dataa = asciitable.read("runa.dat")
datab = asciitable.read("runb.dat")
datac = asciitable.read("runc.dat")

def plot_vs_j():
    fig, (ax1,ax2) = plt.subplots(2,1, sharex=True)
    ax1.plot(data['j'],data['a'])
    ax1.set_ylabel("a")
    ax2.plot(data['j'],data['b'])
    ax2.set_ylabel("b")
    ax2.set_xlabel("j")

    plt.savefig('param_vs_j.eps')

def plot_2d():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data['a'],data['b'],'b',lw=0.2)
    ax.plot(data['a'],data['b'],"bo")
    ax.set_xlabel("a")
    ax.set_ylabel("b")
    ax.fill([0,0,0.45,0.45],[0,0.55,0.55,0],hatch="/",fill=False)
    ax.annotate("Start",(data['a'][0]+0.01,data['b'][0]-0.01))
    ax.annotate("Burn in region",(0.1,0.1))
    fig.savefig("2d_burn_in.eps")

def plot_2d_all():
    A_grid = np.load("A.npy")
    B_grid = np.load("B.npy")
    L = np.load("L.npy")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    CS = ax.contour(A_grid,B_grid,L)
    ax.clabel(CS, inline=1, fontsize=10,fmt = '%2.0f')
    ax.plot(dataa['a'],dataa['b'],'b',lw=0.2)
    ax.plot(dataa['a'],dataa['b'],"bo",label="A")
    ax.plot(datab['a'],datab['b'],'g',lw=0.2)
    ax.plot(datab['a'],datab['b'],"go",label="B")
    ax.plot(datac['a'],datac['b'],'r',lw=0.2)
    ax.plot(datac['a'],datac['b'],"ro",label="C")
    ax.set_xlabel("a")
    ax.set_ylabel("b")
    ax.legend(loc="lower right")
    fig.savefig("2d_all.eps")

def calc_mean_and_sigma():
    burn_in = 100
    mean_a = np.mean(data["a"][burn_in:])
    mean_b = np.mean(data["b"][burn_in:])
    sigma_a = np.std(data["a"][burn_in:])
    sigma_b = np.std(data["b"][burn_in:])
    print("a = %.3f +- %.3f" % (mean_a, sigma_a))
    print("b = %.3f +- %.3f" % (mean_b, sigma_b))
    print("Acceptance Ratio %.2f" % (len(np.where(data['accept'][burn_in:] == 'True')[0])/len(data['accept'][burn_in:])),)

def hist_param():
    fig, (ax1,ax2) = plt.subplots(2,1)
    ax1.hist(data["a"],normed=True,bins=20)
    ax1.set_xlabel("a")
    ax1.set_title("Distribution of a")
    ax1.set_ylabel("Percentage")
    ax2.hist(data["b"],normed=True,bins=20)
    ax2.set_xlabel("b")
    ax2.set_ylabel("Percentage")
    ax2.set_title("Distribution of b")
    fig.subplots_adjust(hspace=0.5)
    plt.savefig('hist_param.eps')


#plot_vs_j()
#calc_mean_and_sigma()
#hist_param()
#ax = plot_2d()
plot_2d_all()
