import numpy as np
from math import *
from math import log as ln
from math import log10 as log
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw(start_range, end_range, N, DRAWTYPE, fx, RSUMTYPE):
    end_range += .1
    rect_linewidth = 1
    # TODO change floats later
    x_vals = np.arange(float(start_range), end_range, .1)
    yValEquation = []
    xValSum = []
    yValSum = []

    def equation(x):  # fix later
        return eval(fx)

    fig, ax = plt.subplots()
    currentAxis = plt.gca()
    deltaX = (end_range-.1)-start_range
    rectangle_length = deltaX/N
    for x in x_vals:  # stores the y values corresponding to the array of x values
        try:
            yValEquation.append(eval(fx))
        except (NameError, SyntaxError):
            return False  # Allows main to show error

    # Draws Rectangles
    if(RSUMTYPE == "Left" and DRAWTYPE):
        for i in np.arange(start_range, end_range-.1, (rectangle_length)):  # LEFT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i, 0), (rectangle_length), equation(i),
                linewidth=rect_linewidth, edgecolor='r', facecolor='none'))

    elif(RSUMTYPE == "Right" and DRAWTYPE):
        for i in np.arange(end_range-.1, start_range, -(rectangle_length)):  # RIGHT RIEMANN SUMS
            currentAxis.add_patch(patches.Rectangle(
                (i-(rectangle_length), 0), (rectangle_length), equation(i), 
                linewidth=rect_linewidth, edgecolor='r', facecolor='none'))

    elif(RSUMTYPE == "Middle" and DRAWTYPE):
        # MIDDLE RIEMANN SUMS
        for i in np.arange(start_range+(rectangle_length)/2, end_range-.1, (rectangle_length)):
            currentAxis.add_patch(patches.Rectangle(
                (i-(rectangle_length)/2, 0), (rectangle_length), equation(i), 
                linewidth=rect_linewidth, edgecolor='r', facecolor='none'))

    if(not DRAWTYPE):  # TRAPEZOID

        for i in np.arange(start_range, end_range-.1, (rectangle_length)):
            # BL,BR,TR, TL order of how nump draws the polygons
            x = [i, i+rectangle_length, i+rectangle_length, i, ]
            y = [0, 0, equation(i+rectangle_length), equation(i)]
            currentAxis.add_patch(patches.Polygon(xy=list(zip(
                x, y)), fill=False, linewidth=rect_linewidth, edgecolor='r', facecolor='none'))

    ax.grid(linewidth='.25')
    ax.set_axisbelow(True)
    plt.plot(x_vals, yValEquation)
    plt.plot(xValSum, yValSum, 'r')
    plt.ylabel('y values')
    plt.xlabel('x values')

    plt.show()


if __name__ == "__main__":
    pass
