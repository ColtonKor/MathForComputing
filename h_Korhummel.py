##MATH270 Program 1
## Colton Korhummel

import matplotlib.pyplot as plt
import random
import csv



def hist(ax, values, x_label, title='', y_label='Frequency'):
    m = max(values)
    h = [0] * (m+1)
    for value in values:
        h[value] += 1

    ax.bar(range(m+1),h)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    if len(title) > 0:
        ax.set_title(title)
    


def part1(ax):
    count=0
    values=[]
    with open('batch-yields-1.csv') as f:
        reader = csv.reader(f)
        for line in reader:
            count+=1
            if(count==1):
                continue
            else:
                values.append(int(line[0]))
    hist(ax, values, 'Yields')



def part2(ax):
    values = []
    for i in range(100):
        values.append(random.randint(1,12))
    hist(ax, values, 'Die')


def part3(ax):
    values = []
    count = 0
    with open('COVID-19_Case_Surveillance_sample.csv') as f:
        reader = csv.reader(f)    
        for line in reader:
            count += 1
            if(count == 1):
                continue
            else:
                date = line[0]
                year, month = date.split('-')
                value = (int(year) - 2020) * 12 + (int(month) - 1)
                values.append(value)
        hist(ax, values, 'COVID cases reported to CDC by Month')


def part4a(ax):
    valuesCA = []
    count = 0
    with open('COVID-19_Case_Surveillance_sample.csv') as f:
        reader = csv.reader(f)    
        for line in reader:
            count += 1
            if(count == 0):
                continue
            else:
                date = line[0]
                year, month = date.split('-')
                value = (int(year) - 2020) * 12 + (int(month) - 1)
                state = line[1]
                if(state == 'CA'):
                    valuesCA.append(value)
        hist(ax, valuesCA, 'COVID California')   

def part4b(ax):
    valuesFL = []
    count = 0
    with open('COVID-19_Case_Surveillance_sample.csv') as f:
        reader = csv.reader(f)    
        for line in reader:
            count += 1
            if(count == 0):
                continue
            else:
                date = line[0]
                year, month = date.split('-')
                value = (int(year) - 2020) * 12 + (int(month) - 1)
                state = line[1]
                if(state == 'FL'):
                    valuesFL.append(value)
        hist(ax, valuesFL, 'COVID Florida')




fig, axes=plt.subplots(3,2)
plt.subplots_adjust(hspace=1)
part1(axes[0,0])
part2(axes[0,1])
part3(axes[1,0])
part4a(axes[1,1])
part4b(axes[2,0])
plt.show()