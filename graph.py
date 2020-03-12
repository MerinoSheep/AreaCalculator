import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy
import math


def draw(STARTRANGE,ENDRANGE,N,DRAWTYPE):
    ENDRANGE += .1
    xValEquation = []
    yValEquation = []
    xValSum = []
    yValSum = []
    RSUMTYPE = "RIGHT" #MIDDLE,LEFT,OR RIGHT
    # The y values for the riemman sum will be stored here
    
    def equation(i):
        return math.cos(i)

    fig, ax = plt.subplots()
    currentAxis = plt.gca()
    deltaX = (ENDRANGE-.1)-STARTRANGE

    for i in numpy.arange(STARTRANGE, ENDRANGE, .1): # Two arrays are stored, one for x values of the equation and another for the y values
        xValEquation.append(i)
        yValEquation.append(equation(i))

    if(RSUMTYPE == "LEFT" and DRAWTYPE ):
        for i in numpy.arange(STARTRANGE, ENDRANGE-.1, (deltaX/N)):  # LEFT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i, 0), (deltaX/N), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            #print(i)
    elif(RSUMTYPE == "RIGHT"):
        for i in numpy.arange(ENDRANGE-.1,STARTRANGE,-(deltaX/N)):  # RIGHT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i-(deltaX/N), 0), (deltaX/N), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            #print(i)

    elif(RSUMTYPE == "MIDDLE"):
        for i in numpy.arange(STARTRANGE+(deltaX/N)/2, ENDRANGE-.1,(deltaX/N)):  # MIDDLE RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i-(deltaX/N)/2, 0), (deltaX/N), equation(i), linewidth=1, edgecolor='r', facecolor='none'))
            print(i)

    if(not DRAWTYPE): ## TRAPEZOID

        for i in numpy.arange(STARTRANGE, ENDRANGE-.1, (deltaX/N)):
            x=[i,i+deltaX/N,i+deltaX/N,i,] #BL,BR,TR, TL
            y=[0,0,equation(i+deltaX/N),equation(i)]
            currentAxis.add_patch(patches.Polygon(xy=list(zip(x,y)),fill= False, linewidth=1, edgecolor='r', facecolor='none'))
    # print(xValEquation)
    plt.plot(xValEquation, yValEquation)
    plt.plot(xValSum, yValSum, 'r')
    plt.ylabel('y values')
    plt.xlabel('x values')
    plt.show()

if __name__ == "__main__":
    draw()
