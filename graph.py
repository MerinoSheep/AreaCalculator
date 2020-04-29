import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from math import *


def draw(STARTRANGE,ENDRANGE,N,DRAWTYPE,fx,RSUMTYPE):
    ENDRANGE += .1
    x_vals = np.arange(float(STARTRANGE),ENDRANGE,.1) ## change floats later
    yValEquation = []
    xValSum = [] ## Rectangles or Trapezoids
    yValSum = []  ## ^
    
    def equation(i):
        x=i
        return eval(fx)

    fig, ax = plt.subplots()
    currentAxis = plt.gca()
    deltaX = (ENDRANGE-.1)-STARTRANGE
    rectangle_length = deltaX/N


    for x in x_vals: #stores the y values corresponding to the array of x values
        yValEquation.append(eval(fx))

   

    #Draws Rectangles
    if(RSUMTYPE == "LEFT" and DRAWTYPE ):
        for i in np.arange(STARTRANGE, ENDRANGE-.1, (rectangle_length)):  # LEFT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i, 0), (rectangle_length), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            #print(i)
    elif(RSUMTYPE == "RIGHT" and DRAWTYPE):
        for i in np.arange(ENDRANGE-.1,STARTRANGE,-(rectangle_length)):  # RIGHT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i-(rectangle_length), 0), (rectangle_length), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            #print(i)

    elif(RSUMTYPE == "MIDDLE"and DRAWTYPE):
        for i in np.arange(STARTRANGE+(rectangle_length)/2, ENDRANGE-.1,(rectangle_length)):  # MIDDLE RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i-(rectangle_length)/2, 0), (rectangle_length), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            print(i)

    if(not DRAWTYPE): ## TRAPEZOID

        for i in np.arange(STARTRANGE, ENDRANGE-.1, (rectangle_length)):
            x=[i,i+rectangle_length,i+rectangle_length,i,] #BL,BR,TR, TL order of how nump draws the polygons 
            y=[0,0,equation(i+rectangle_length),equation(i)]
            currentAxis.add_patch(patches.Polygon(xy=list(zip(x,y)),fill= False, linewidth=1, edgecolor='r', facecolor='none'))
    # print(x_vals)
    plt.plot(x_vals, yValEquation)
    plt.plot(xValSum, yValSum, 'r')
    plt.ylabel('y values')
    plt.xlabel('x values')
    plt.show()

if __name__ == "__main__":
    pass
