import matplotlib.pyplot as plt
import numpy as np
import math
from AnimationClassStudents import Matrix

def animation(house):
    Mh = Matrix(house)


# initialize plotting system
    plt.ion()

# plot house , pause 1 seconds   
    Mh.plot()
    plt.pause(1.0)

# My code Starts
    # Shear test
    Mh.shear(dx = .5, dy = .5)
    Mh.plot(clrfig=0)
    plt.pause(1.0)

    Mh = Matrix(house)

    Mh.plot()
    plt.pause(1.0)


    # Scale test
    Mh.scale(dx = .5, dy = .5)
    Mh.plot(clrfig=0)
    plt.pause(1.0)

    Mh = Matrix(house)

    Mh.plot()
    plt.pause(1.0)

    # Reflects over x axis
    Mh.reflect(axis = 'x')
    Mh.plot(clrfig=0)
    plt.pause(1.0)

    Mh = Matrix(house)

    Mh.plot()
    plt.pause(1.0)

    # y = -x
    Mh.reflect(axis = 'z')
    Mh.plot(clrfig=0)
    plt.pause(1.0)

    Mh = Matrix(house)

    Mh.plot()
    plt.pause(1.0)
# My code Ends



# rotate 60 degrees about the origin
    Mh.rotate(math.pi/3.0, about='origin')

# replot rotated figure, do not clear the screen
    Mh.plot(clrfig=0)   
    plt.pause(1.0)

# reset figure
    Mh = Matrix(house)
# plot house,  pause 1 seconds   
    Mh.plot( )  #  erases screen 
    plt.pause(1.0)

# rotate 60 degrees about the center
    Mh.rotate(-math.pi/3.0, about='point')

# plot rotated house, pause 1 seconds   
    Mh.plot(clrfig=0)   
    plt.pause(1.0)

    Mh = Matrix(house)
    Mh.plot()
    Mh.rotate(-math.pi/3.0, about='center')
    Mh.plot(clrfig=0)   
    plt.pause(1.0)

# translate animate
# clear screen on each plot
# pause for less than 1/32 seconds
    Mh = Matrix(house)
    Mh.plot()  
    # this reflects matrix over y so we can see the whole translation
    Mh.reflect(axis = 'y')
    Mh.plot(clrfig=0)
    plt.pause(1.0)
    Mh.plot()   
    plt.pause(1.0)
    for i in range(35):
        Mh.translate(.5, 0)
        Mh.plot(clrfig=1)   
        plt.pause(1/35)

# # create 2d figure of square house and triangle roof
# #  first row is x coordinates, second row is y cooridnates
# #  trace all vertices of the figure 
# # shape1 = np.matrix('0. 0. 20. 20. 0. 10. 20; 20. 0. 0. 20. 20. 30. 20.')
shape1 = np.matrix('-10. 0. 10. -10.; 10. 30. 10. 10.')
shape2 = np.matrix('0. 10. 20. 30. 30. 20. 10. 0. 0.; 10. 0. 0. 10. 20. 30. 30. 20. 10.')
animation(shape1)
animation(shape2)
print("Colton Korhummel") 