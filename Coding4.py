import matplotlib.pyplot as plt
import math
import random
import numpy as np

def hist(ax, values, x_label, title='', y_label='Frequency', density=False, bin_w=0.0, bin_start=0.0):
    m = max(values)
    if bin_w == 0:
        h = [0] * (m+1)
        for value in values:
            h[value] += 1
    elif bin_w > 0:
        nbins = int(((m-bin_start)/bin_w)+1)
        h = [0]*nbins
        x_axis = [0]*nbins
        for i in range(nbins):
            x_axis[i] = bin_start+bin_w*i

        for x in values:
            ibin = int((x-bin_start)/bin_w)
            h[ibin] += 1
    if density==True:
        for i in range(len(h)):
            h[i] = h[i]/len(values)
    ax.bar(x_axis,h,width =bin_w,align='edge')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if len(title) > 0:
        ax.set_title(title)

def test2(x):
    return (1.0/3.0)*x**3

def test3(x):
    return math.sin(x)+1

def integrate(f, a, b, n):
    dx=float(b-a)/float(n)
    totalarea=float(f(a))/2 + float(f(b))/2
    for i in range(1,n):
        totalarea+=f(a+i*dx)
        totalarea= totalarea*dx
    return totalarea

def random3xsq():
    x=random.random()
    r=x**(1/3)
    return r

# Part 1
a = 0
b = 2*math.pi #Change these values to get answers.
correct = 2*math.pi
n=1
ans=0.0
while (abs(ans-correct) > .01):
    n=n*2
    ans=integrate(test3, a, b, n)
    print('n=%d ans=%.2f'%(n,ans))

# Part 2
fig,ax1 = plt.subplots()
values = []
for x in range(1000000):
    values.append(random3xsq())
hist(ax1, values, x_label = "x", title = "Random value from distribution with pdf(x)=3x**2", density=True, y_label="probability", bin_w=.01, bin_start=0)
plt.show()

