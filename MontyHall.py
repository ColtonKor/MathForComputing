import random

def Stay():
    wins = 0
    for _ in range(1000):
        prize = random.randint(1, 3)
        contestant = random.randint(1, 3)
        if prize == contestant:
            wins += 1
    return wins


def Switch():
    wins = 0
    for _ in range(1000):
        prize = random.randint(1, 3)
        contestant = random.randint(1, 3)
        remaining = [door for door in [1, 2, 3] if door != contestant and door != prize]
        # remaining = []
        # for door in [1, 2, 3]:
        #     if door != contestant and door != prize:
        #         remaining.add[door]

        if prize != contestant:
            open = remaining[0]
        else:
            open = random.choice(remaining)
        doors = [1, 2, 3]
        doors.remove(contestant)
        doors.remove(open)
        switch = doors[0]
        if switch == prize:
            wins += 1
    return wins



staying = Stay()
print("Number of wins:", staying)
switching = Switch()
print("Number of wins with switching:", switching)

# It is better for the contestant to switch doors because as you see in the output when you switch you win aproximately 
# 2x more than if you stay at your door.