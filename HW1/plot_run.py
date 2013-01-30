import asciitable
import matplotlib.pyplot as plt
import numpy as np


data = asciitable.read("run.dat")

def plot_vs_j():
    fig, (ax1,ax2) = plt.subplots(2,1, sharex=True)
    ax1.plot(data['j'],data['a'])
    ax1.set_ylabel("a")
    ax2.plot(data['j'],data['b'])
    ax2.set_ylabel("b")
    ax2.set_xlabel("j")

    plt.savefig('param_vs_j.eps')

def calc_mean_and_sigma():
    burn_in = 100
    mean_a = np.mean(data["a"][100:])
    mean_b = np.mean(data["b"][100:])
    sigma_a = np.std(data["a"][100:])
    sigma_b = np.std(data["b"][100:])
    print(mean_a,mean_b)
    #0.496544331108 0.605182354303
    print(sigma_a,sigma_b)
    #0.0195820063105 0.0403324627735

def hist_param():
    fig, (ax1,ax2) = plt.subplots(2,1)
    ax1.hist(data["a"])
    ax1.set_xlabel("a")
    ax1.set_title("Distribution of a")
    ax1.set_ylabel("Frequency")
    ax2.hist(data["b"])
    ax2.set_xlabel("b")
    ax2.set_ylabel("Frequency")
    ax2.set_title("Distribution of b")
    fig.subplots_adjust(hspace=0.5)
    plt.savefig('hist_param.eps')

#calc_mean_and_sigma()
#hist_param()
