from math import *  # pylint: disable=unused-wildcard-import disable=wildcard-import
from math import log as ln  # pylint: disable=unused-import
from math import log10 as log  # pylint: disable=unused-import
from tkinter import Label, Toplevel
from typing import Union
import scipy.integrate
import numpy as np



class IntegralWindow(Toplevel):
    '''Creates Toplevel window for integral and sum solutions'''
    def __init__(self, startrange: float, endrange: float, n: int, fx: str) -> None:
        Toplevel.__init__(self)
        self.title("Integral")
        self.geometry("300x180")
        self.startrange = startrange
        self.endrange = endrange
        self.n = n
        self.fx = fx
        self.integrate_label = Label(self, text="Integral:")
        self.integrate_answer = Label(self)

        self.width = (self.endrange - self.startrange)/n
        # left riemann sum
        self.lr_sum_label = Label(self, text="Left Riemann Sum:")
        self.lr_sum = Label(self)
        # right riemann sum
        self.rr_sum = Label(self)
        self.rr_sum_label = Label(self, text="Right Riemann Sum")
        # middle riemann sum
        self.mr_sum_label = Label(self, text="Middle Riemann Sum")
        self.mr_sum = Label(self)
        # Trapezoid sum
        self.trpz_sum_label = Label(self, text="Trapezoidal Sum")
        self.trpz_sum = Label(self, text=self.trapezoid(self.fx))

        self.integrate(startrange, endrange, n, fx)
        self.grid_layout()

    def grid_layout(self) -> None:
        '''Grids labels'''
        self.integrate_label.grid(row=0, column=0)
        self.integrate_answer.grid(row=0, column=1)
        self.lr_sum_label.grid(row=1, column=0)
        self.lr_sum.grid(row=1, column=1)
        self.rr_sum_label.grid(row=2, column=0)
        self.rr_sum.grid(row=2, column=1)
        self.mr_sum_label.grid(row=3, column=0)
        self.mr_sum.grid(row=3, column=1)
        self.trpz_sum_label.grid(row=4, column=0)
        self.trpz_sum.grid(row=4, column=1)


    def integrate(self, startrange: float, endrange: float, n: int, fx: str) -> None:
        '''Calls riemann and trapezoid and does integration'''
        self.function = eval(f"lambda x:{fx}")
        self.i = scipy.integrate.quad(
            self.function, self.startrange, self.endrange)
        self.integrate_answer['text'] = str(self.i[0])
        # left riemann sum
        self.lr_sum['text'] = self.riemann(
            self.startrange, self.endrange, self.n, self.fx, self.width)
        # right riemann sum
        self.rr_sum['text'] = self.riemann(
            endrange, startrange, n, fx, self.width)
        # middle riemann sum
        self.mr_sum['text'] = self.riemann(
            startrange+self.width/2, (self.endrange+self.width/2), n, fx, self.width)

    def func(self, x: float, fx: str) -> Union[int, float]:
        '''evaluates function at the given x value'''
        return eval(fx)

    def riemann(self, startrange: float, endrange: float, N: int, fx: str, width: float):
        '''returns sum of a given riemann given parameters'''
        points = np.linspace(startrange, endrange, num=N, endpoint=False)
        func_points = []
        for i in points:
            func_points.append(self.func(i, fx))
        func_points = np.asarray(func_points)
        indv_area = func_points*width
        return np.sum(indv_area)

    def trapezoid(self, fx):
        '''returns sum of area using trapezoids'''
        points = np.arange(self.startrange, self.endrange, self.width)
        points = np.append(points, self.endrange)
        func_points = []
        for i in points:
            func_points.append(self.func(i, fx))
        ans = np.trapz(func_points, dx=self.width)
        return ans

if __name__ == "__main__":
    pass
