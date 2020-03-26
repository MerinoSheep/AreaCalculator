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


    for x in x_vals: # Two arrays are stored, one for x values of the equation and another for the y values
        yValEquation.append(eval(fx))

   

    #Draws Rectangles
    if(RSUMTYPE == "LEFT" and DRAWTYPE ):
        for i in np.arange(STARTRANGE, ENDRANGE-.1, (deltaX/N)):  # LEFT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i, 0), (deltaX/N), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            #print(i)
    elif(RSUMTYPE == "RIGHT" and DRAWTYPE):
        for i in np.arange(ENDRANGE-.1,STARTRANGE,-(deltaX/N)):  # RIGHT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i-(deltaX/N), 0), (deltaX/N), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            #print(i)

    elif(RSUMTYPE == "MIDDLE"and DRAWTYPE):
        for i in np.arange(STARTRANGE+(deltaX/N)/2, ENDRANGE-.1,(deltaX/N)):  # MIDDLE RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i-(deltaX/N)/2, 0), (deltaX/N), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            print(i)

    if(not DRAWTYPE): ## TRAPEZOID

        for i in np.arange(STARTRANGE, ENDRANGE-.1, (deltaX/N)):
            x=[i,i+deltaX/N,i+deltaX/N,i,] #BL,BR,TR, TL
            y=[0,0,equation(i+deltaX/N),equation(i)]
            currentAxis.add_patch(patches.Polygon(xy=list(zip(x,y)),fill= False, linewidth=1, edgecolor='r', facecolor='none'))
    # print(x_vals)
    plt.plot(x_vals, yValEquation)
    plt.plot(xValSum, yValSum, 'r')
    plt.ylabel('y values')
    plt.xlabel('x values')
    plt.show()

if __name__ == "__main__":
    draw()
