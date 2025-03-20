import numpy as np
import random

def partA(diagnosed):
    m = (12 - 92)/(36 - 9)
    b = 92 - (m*9)
    if diagnosed <= 9:
        return 92
    elif diagnosed >= 36:
        return 12
    else:
        return (m * diagnosed) + b
    
def partB(age):
    return np.random.exponential(scale=age)

def partC(trials, type):
    rates = []
    for i in range(trials):
        if type == 1:
            diag = random.randint(1, 24)
        elif type == 2:
            diag = random.randint(24, 48)
        rates.append(partA(diag))
    Survival = np.mean(rates)
    return Survival




diagnosed = random.randint(1, 36)
trials = 100
age = 150
rate = partA(diagnosed)
developed = [trials]
for i in range(trials):
    developed.append(partB(age))
Under75 = np.mean(np.array(developed) <= 75)*100
Annual = partC(trials, 1)
Biannual = partC(trials, 2)
print(f"Survival rate after {diagnosed:.2f} months: {rate:.2f}%")
print(f"People developing disease before age 75: {Under75:.2f}%")
print(f"Survival with Annual insurance: {Annual:.2f}%")
print(f"Survival with Biannual insurance: {Biannual:.2f}%")

