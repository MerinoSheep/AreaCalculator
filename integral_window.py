import tkinter as tk
import scipy.integrate
import numpy as np


class IntegralWindow(tk.Toplevel):
    def __init__(self, startrange, endrange, n, fx):
        tk.Toplevel.__init__(self)
        #self.master =master
        self.title("windowdd")
        self.geometry("200x180")
        self.startrange = startrange
        self.endrange = endrange
        self.n = n
        self.fx = fx
        self.integrate_label = tk.Label(self, text="Integral:")
        self.integrate_answer = tk.Label(self)

        self.width = (self.endrange - self.startrange)/n
        # left riemann sum
        self.lr_sum_label = tk.Label(self, text="Left Riemann Sum:")
        self.lr_sum = tk.Label(self)


        #right riemann sum
        self.rr_sum = tk.Label(self)
        self.rr_sum_label = tk.Label(self, text="Right Riemann Sum")


        #middle riemann sum
        self.mr_sum_label = tk.Label(self, text="Middle Riemann Sum")
        self.mr_sum = tk.Label(self)


        #Trapezoid sum
        self.trpz_sum_label = tk.Label(self, text="Trapezoidal Sum")
        self.trpz_sum = tk.Label(self, text =self.trapezoid(self.fx))

        self.integrate(startrange, endrange, n, fx)
        self.grid()

    def grid(self):
        self.integrate_label.grid(row=0, column=0)
        self.integrate_answer.grid(row=0, column=1)
        self.lr_sum.grid(row=1, column=1)
        self.lr_sum_label.grid(row=1, column=0)
        self.rr_sum_label.grid(row=2, column=0)
        self.rr_sum.grid(row=2, column=1)
        self.trpz_sum_label.grid(row=4,column=0)
        self.trpz_sum.grid(row=4,column=1)
        self.mr_sum_label.grid(row=3, column=0)
        self.mr_sum.grid(row=3, column=1)

    def integrate(self, startrange, endrange, N, fx):

        self.function = eval("lambda x:{}".format(fx))
        self.i = scipy.integrate.quad(self.function, self.startrange, self.endrange)
        self.integrate_answer['text'] = str(self.i[0])
        # left riemann sum
        self.lr_sum['text'] = self.riemann(self.startrange, self.endrange, self.n, self.fx, self.width)
        # right riemann sum
        self.rr_sum['text'] = self.riemann(
            endrange, startrange, N, fx, self.width)
        # middle riemann sum
        self.mr_sum['text'] = self.riemann(
            startrange+self.width/2, (self.endrange+self.width/2), N, fx, self.width)
        # Trapezoid Sum

    def func(self,x, fx):
        return eval(fx)

    def riemann(self, startrange, endrange, N, fx, width):
        points = np.linspace(startrange, endrange, num=N, endpoint=False)
        func_points = []
        for i in points:
            func_points.append(self.func(i, fx))
        func_points = np.asarray(func_points)
        indv_area = func_points*width
        return np.sum(indv_area)


    def trapezoid(self,fx):
        #print(self.width)
        points = np.arange(self.startrange, self.endrange, self.width)
        points = np.append(points, self.endrange)
        print(points)
        func_points = []
        for i in points:
            func_points.append(self.func(i, fx))
        #print(func_points)
        ans = np.trapz(func_points, dx=self.width)
        return ans


'''
def run(startrange, endrange, n, fx):
    root = tk.Tk()
    IntegralWindow(root, startrange, endrange, n,fx)
    #integral_window.integrate(0, 5, 10, '2*x')
    root.mainloop()
'''


if __name__ == "__main__":
    #run(0,5,4,'2*x')
    pass
