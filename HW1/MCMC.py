import asciitable
import numpy as np

#Read in data
data = asciitable.read("ps_1_data_set.txt")
xi = data["x_i"]
yi = data["y_i"]

def model(x,a,b):
    return a + b * x

def chi_sq(a,b,sigma):
    return np.sum(((yi - model(xi,a,b))/sigma)**2)

def r(a_cur,b_cur,a_prev,b_prev,sigma):
    #a_cur is a_{j} and a_prev is a_{j-1}
    return np.exp(-(chi_sq(a_cur,b_cur,sigma) - chi_sq(a_prev,b_prev,sigma))/2.)

a_old = 0.0
b_old = 1.0
sigma = 0.08

def run_chain():
    sequences = []
    global a_old, b_old, sigma
    for j in range(1000):
        #take jump
        accept = False
        a_jump = np.random.normal(scale=0.03)
        b_jump = np.random.normal(scale=0.05)
        a_new = a_old + a_jump
        b_new = b_old + b_jump
        ratio = r(a_new,b_new,a_old,b_old,sigma)
        if ratio >= 1.0:
            a_old = a_new
            b_old = b_new
            accept = True
        else:
            u = np.random.uniform()
            if ratio >= u:
                a_old = a_new
                b_old = b_new
                accept = True
        sequences.append([j,ratio,accept,a_old,b_old])

    asciitable.write(sequences,"runa.dat",names=["j","ratio","accept","a","b"])

run_chain()
