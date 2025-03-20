import matplotlib.pyplot as plt
import numpy as np
import math

class Matrix:

    """ ------------------------------------------------------
    :: Initialization stuff....no need to modify
    ------------------------------------------------------
    """
    def __init__(self, matrix):     # Note: We must add a row of ones in order to make use of translation transformation
        self.matrix = matrix
        onesRow = np.ones(self.matrix.shape[1])
        self.matrix = np.vstack((self.matrix, onesRow))
        
    """
    ------------------------------------------------------
     :: Rotation Transformation
 	  Arguments: 
 	      theta: rotate object theta radians (default: 0)
          Possible Arguments: 
	      about:  Rotate about different axes...i.e. about origin , about a point (default: origin)
    ------------------------------------------------------
    """
    
    def rotate(self, radians,about='origin'):
        cos_t = math.cos(radians)
        sin_t = math.sin(radians)
        if about == 'origin':
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
        elif about == 'point':
            xpoint = self.matrix[0,0]
            ypoint = self.matrix[1,0]
            self.translate(-xpoint,-ypoint)
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
            self.translate(xpoint,ypoint)

        elif about == 'center':
            xpoint = np.mean(self.matrix[0,:])
            ypoint = np.mean(self.matrix[1,:])
            self.translate(-xpoint,-ypoint)
            self.matrix = np.matrix(' %s %s  0;'
                                    ' %s %s  0;'
                                    '  0  0  1' % (cos_t, -sin_t, sin_t, cos_t)) * self.matrix
            self.translate(xpoint,ypoint)
            
    """
     ------------------------------------------------------
     :: Translate Transformation
        Arguments: 
           dx : Translate in x direction  (Default: 0)
    	   dy : Translate in y direction (Default: 0)

     ------------------------------------------------------
    """
     
    def translate(self, dx=0, dy=0):
        self.matrix = np.matrix(' 1  0 %s;'
                                ' 0  1 %s;'
                                ' 0  0  1' % (dx, dy)) * self.matrix

    """
     ------------------------------------------------------
     :: Scale Transformation
         Arguments: 
           dx : Scale in x direction
    	   dy : Scale in y direction

     ------------------------------------------------------
    """
    
    def scale(self, dx=1, dy=1):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!! INSERT SCALE CODE HERE !!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.matrix = np.matrix('%s 0 0; '
                                '0 %s 0; '
                                '0 0 1 ' % (dx, dy)) * self.matrix

    """
      ------------------------------------------------------
     # :: Reflect Transformation
     #    Possible Arguments: 
     #       axis : axis to reflect object about
     #
     # ------------------------------------------------------
    """
    
    def reflect(self, axis = 'y'):
        if axis == 'x':
            # REFLECT ABOUT X-AXIS
            self.matrix = np.matrix(' 1  0  0;'
                                    ' 0 -1  0;'
                                    ' 0  0  1' ) * self.matrix
        elif axis == 'y':
            # REFLECT ABOUT Y-AXIS  
            self.matrix = np.matrix('-1  0  0;'
                                    ' 0  1  0;'
                                    ' 0  0  1' ) * self.matrix
        elif axis == 'z':
            self.matrix = np.matrix(' 0  -1  0;'
                                    ' -1  0  0;'
                                    ' 0  0  1' ) * self.matrix
           
    """
     # ------------------------------------------------------
     # :: Shearing Transformation
     #    Arguments: 
     #  dx : Shear in x direction  
     #	dy : Shear in y direction  
     #
     # ------------------------------------------------------
    """
    def shear(self, dx=0, dy=0):

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!! INSERT SHEAR CODE HERE !!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.matrix = np.matrix(' 1 %s 0; '
                                ' %s 1 0;'
                                ' 0 0 1' % (dx, dy)) * self.matrix


    """
     # :: Plot object. 
     #    Optional Arguments:  (You may modify these values)
     #       - 'clrfig' : Clear figure before plotting (default 1)
     #	- 'xMin'/'xMax' : Plot limits for x-values (default: -40,40) 
     # 	- 'yMin'/'yMax' : Plot limits for y-values (default: -40,40)
     #
    """
    def plot(self, clrfig=1,xMin=-40,xMax=40,yMin=-40,yMax=40):   
        if clrfig == 1:
            plt.gcf().clear()
        plt.plot(np.transpose(self.matrix[0, :]), np.transpose(self.matrix[1, :]))
        plt.xlim(xMin, xMax)       
        plt.ylim(yMin, yMax)
        plt.show()