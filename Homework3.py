import matplotlib.pyplot as plt
import random
import csv

def hist(ax, values, x_label, title='', y_label='Frequency', density=False, bin_w=0.0, bin_start=0.0):
    m = max(values)
    if bin_w == 0:
        h = [0] * (m+1)
        for value in values:
            h[value] += 1

        # ax.bar(range(m+1),h)
    elif bin_w > 0:
        # x = bin_start
        # numbins = 0
        # while(x < m):
        #     x += bin_w
        #     numbins += 1


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

        # ax.bar(x_axis, h)
    ax.bar(x_axis,h,width =bin_w,align='edge')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if len(title) > 0:
        ax.set_title(title)



def part1(ax):
    values = []
    for i in range(100):
        values.append(random.random())
    hist(ax, values, 'Random Values', y_label = 'Probability Density', density=True, bin_w=0.1, bin_start=0.0)
    



def part2(ax):
    fin=open('Apr25_27thAn_set1.shtml')
    paces=[]
    for line in fin:
        if(len(line)>=41 and line[40]==':' and line[39]>='0' and line[39] <='9'):
            secs = int(line[41:43])+int(line[38:40])*60
            #calulate MPH
            speed = 1/secs
            mph = speed*3600
            paces.append(mph)
    hist(ax, paces, 'Miles Per Hour', y_label = 'Probability Density', density=True, bin_w=0.3, bin_start=0.0)



fig, axes=plt.subplots(2,2)
plt.subplots_adjust(hspace=1)
plt.subplots_adjust(wspace=0.5)
part1(axes[0,0])
part2(axes[0,1])
plt.show()