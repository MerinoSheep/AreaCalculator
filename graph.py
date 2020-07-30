'''graph.py'''

from math import *  # pylint: disable=unused-wildcard-import disable=wildcard-import
import configparser
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import numexpr as ne

def draw(start_range: float, end_range: float, N: int, fx: str, drawtype: bool, RSUMTYPE: str, gui: object):
    """Starts graphing equation with sum"""

    linewidth = 1
    x_vals = np.arange(start_range, end_range+.0005, .001)#.001
    def equation(x):  # pylint: disable=unused-argument
        return eval(fx)

    delta_x = (end_range)-start_range
    rectangle_length = delta_x/N
    def is_in_bounds(gui: object) -> bool:
        global y_val_equation
        x = x_vals
        try:
            y_val_equation = ne.evaluate(fx)
        except ZeroDivisionError:
            gui.error_var.set("Function does not exist in range")
            return False
        return True


    if is_in_bounds(gui):
        fig, ax = plt.subplots(nrows=1, ncols=1)
        del fig
        current_axis = plt.gca()
        # Draws Rectangles
        if drawtype is not None and drawtype:
            if RSUMTYPE == "Left":  # LEFT RIEMANN SUMS
                for i in np.arange(start_range, end_range, rectangle_length):
                    current_axis.add_patch(patches.Rectangle(
                        (i, 0), (rectangle_length), equation(i),
                        linewidth=linewidth, edgecolor='r', facecolor='none'))

            elif RSUMTYPE == "Right":  # RIGHT RIEMANN SUMS
                for i in np.arange(end_range, start_range, -(rectangle_length)):
                    current_axis.add_patch(patches.Rectangle(
                        (i-(rectangle_length), 0), rectangle_length, equation(i),
                        linewidth=linewidth, edgecolor='r', facecolor='none'))

            elif RSUMTYPE == "Middle":  # MIDDLE RIEMANN SUMS
                for i in np.arange(start_range+rectangle_length/2, end_range, rectangle_length):
                    current_axis.add_patch(patches.Rectangle(
                        (i-(rectangle_length)/2, 0), rectangle_length, equation(i),
                        linewidth=linewidth, edgecolor='r', facecolor='none'))

        elif drawtype is not None and not drawtype:  # TRAPEZOID
            for i in np.arange(start_range, end_range, (rectangle_length)):
                # BL,BR,TR, TL order of how nump draws the polygons
                x = [i, i+rectangle_length, i+rectangle_length, i, ]
                y = [0, 0, equation(i+rectangle_length), equation(i)]
                poly = patches.Polygon(xy=list(
                    zip(x, y)), fill=False, linewidth=linewidth, edgecolor='r', facecolor='none')
                current_axis.add_patch(poly)
        # Does not graph asymptotes
        utol =  150.
        ltol = -150.
        y_val_equation[y_val_equation > utol] = np.inf
        y_val_equation[y_val_equation < ltol] = -np.inf
        ax.grid(linewidth='.25')
        ax.set_axisbelow(True)
        plt.plot(x_vals, y_val_equation)
        plt.ylabel('y values')
        plt.xlabel('x values')
        config = configparser.ConfigParser()
        config.read('config.ini')
        if not config.getboolean('Y Limits', 'use_auto_values'):
            if config.get('Y Limits', 'y_max') != "None":
                plt.ylim(top=config.getfloat('Y Limits', 'y_max'))
            if config.get('Y Limits', 'y_min') != "None":
                plt.ylim(bottom=config.getfloat('Y Limits', 'y_min' ))
        plt.show()


if __name__ == "__main__":
    pass
