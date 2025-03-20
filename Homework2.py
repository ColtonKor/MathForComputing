import matplotlib.pyplot as plt
import random
import csv



def hist(ax, values, x_label, title='', y_label='Frequency', density = False):
    m = max(values)
    h = [0] * (m+1)
    for value in values:
        h[value] += 1
    if density==True:
        for i in range(len(h)):
            h[i] = h[i]/len(values)

    ax.bar(range(m+1),h)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if len(title) > 0:
        ax.set_title(title)
    


def part1(ax):
    values = []
    for i in range(100):
        values.append(random.randint(1,12))
    hist(ax, values, 'Dice Rolls', density=True)



def part2(ax, axB):
    fin=open('2015_2017_MaleData.dat')
    num=[]
    biased_num=[]
    for line in fin:
        v=int(line[3793])
        num.append(v)
        for x in range(v):
            biased_num.append(v)
    fin.close()
    hist(ax, num, 'Unbiased children in household', density=True)
    hist(axB, biased_num, 'Biased children in household', density=True)





fig, axes=plt.subplots(2,2)
plt.subplots_adjust(hspace=1)
part1(axes[0,0])
part2(axes[0,1], axes[1,0])
plt.show()