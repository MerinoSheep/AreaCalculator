'''graph.py'''

from math import *  # pylint: disable=unused-wildcard-import disable=wildcard-import
from math import log as ln  # pylint: disable=unused-import
from math import log10 as log  # pylint: disable=unused-import
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def draw(start_range: float, end_range: float, N: int, fx: str, drawtype: bool, RSUMTYPE: str, gui: object):
    """Starts graphing equation with sum"""
    end_range += .1
    rect_linewidth = 1
    x_vals = np.arange(float(start_range), end_range, .001)
    y_val_equation = []
    x_val_sum = [] # Arrays for rectangles or trapezoids created
    y_val_sum = []

    def equation(x): # pylint: disable=unused-argument
        return eval(fx)


    delta_x = (end_range-.1)-start_range
    rectangle_length = delta_x/N
    def is_in_bounds(gui):
        for x in x_vals:  # stores the y values corresponding to the array of x values
            try:
                y_val_equation.append(eval(fx))
            except (NameError, SyntaxError):
                gui.error_var.set("Function does not exist in range")
                return False  # Allows main to show error
        return True
    if is_in_bounds(gui):
        fig, ax = plt.subplots()
        del fig
        current_axis = plt.gca()
        # Draws Rectangles
        if drawtype is not None and drawtype:
            if RSUMTYPE == "Left":  # LEFT RIEMANN SUMS
                for i in np.arange(start_range, end_range-.1, rectangle_length):
                    current_axis.add_patch(patches.Rectangle(
                        (i, 0), (rectangle_length), equation(i),
                        linewidth=rect_linewidth, edgecolor='r', facecolor='none'))

            elif RSUMTYPE == "Right":  # RIGHT RIEMANN SUMS
                for i in np.arange(end_range-.1, start_range, -(rectangle_length)):
                    current_axis.add_patch(patches.Rectangle(
                        (i-(rectangle_length), 0), (rectangle_length), equation(i),
                        linewidth=rect_linewidth, edgecolor='r', facecolor='none'))

            elif RSUMTYPE == "Middle":  # MIDDLE RIEMANN SUMS
                for i in np.arange(start_range+rectangle_length/2, end_range-.1, rectangle_length):
                    current_axis.add_patch(patches.Rectangle(
                        (i-(rectangle_length)/2, 0), (rectangle_length), equation(i),
                        linewidth=rect_linewidth, edgecolor='r', facecolor='none'))

        elif drawtype is not None and not drawtype:  # TRAPEZOID
            for i in np.arange(start_range, end_range-.1, (rectangle_length)):
                # BL,BR,TR, TL order of how nump draws the polygons
                x = [i, i+rectangle_length, i+rectangle_length, i, ]
                y = [0, 0, equation(i+rectangle_length), equation(i)]
                current_axis.add_patch(patches.Polygon(xy=list(zip(
                    x, y)), fill=False, linewidth=rect_linewidth, edgecolor='r', facecolor='none'))
        utol = 150.
        ltol = -150.
        y_val_equation = np.array(y_val_equation)  ##TODO change this earlier
        y_val_equation[y_val_equation > utol] = np.inf
        y_val_equation[y_val_equation < ltol] = -np.inf
        ax.grid(linewidth='.25')
        ax.set_axisbelow(True)
        plt.plot(x_vals, y_val_equation)
        plt.plot(x_val_sum, y_val_sum, 'r')
        plt.ylabel('y values')
        plt.xlabel('x values')
        plt.show()


if __name__ == "__main__":
    pass
